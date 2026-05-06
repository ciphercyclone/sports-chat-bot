import os
import asyncio
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in .env file or environment.")

genai.configure(api_key=API_KEY)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

SYSTEM_INSTRUCTION = """
You are SportsBot, a knowledgeable "sideline reporter" — confident, friendly, and fast.
Your domain is strictly sports. Answer general sports questions, including well-established rules, historical records, player comparisons, and tactical analysis.
Provide appropriate disclaimers when relevant (e.g., predictions, injury speculation).
You MUST refuse requests completely unrelated to sports (politics, finance, cooking, etc.), harmful or abusive requests, or content that is inappropriate regardless of domain.
Do NOT refuse routine sports questions by being overly cautious. Be helpful.
Always format your responses in Markdown (bold, italics, lists, etc.).
"""

model = genai.GenerativeModel('gemini-2.5-flash-lite', system_instruction=SYSTEM_INSTRUCTION)

class ChatMessage(BaseModel):
    role: str
    parts: List[dict]

class ChatRequest(BaseModel):
    message: str
    history: List[ChatMessage]

def format_history_for_gemini(history: List[ChatMessage]):
    formatted_history = []
    for msg in history:
        formatted_history.append(
            {"role": "user" if msg.role == "user" else "model", "parts": [msg.parts[0]["text"]]}
        )
    return formatted_history

@app.get("/")
async def root():
    return FileResponse("static/code.html")

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        chat_session = model.start_chat(history=format_history_for_gemini(request.history))
        response = chat_session.send_message(request.message)
        return {"reply": response.text}
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "ResourceExhausted" in error_msg:
            await asyncio.sleep(2)
            try:
                chat_session = model.start_chat(history=format_history_for_gemini(request.history))
                response = chat_session.send_message(request.message)
                return {"reply": response.text}
            except Exception:
                return JSONResponse(status_code=429, content={"reply": "SportsBot is busy right now — try again in a moment."})
        elif "403" in error_msg or "PermissionDenied" in error_msg or "API_KEY_INVALID" in error_msg:
            return JSONResponse(status_code=403, content={"reply": f"API error: {error_msg}"})
        else:
            print(f"Error: {e}")
            return JSONResponse(status_code=500, content={"reply": "Something went wrong — please retry."})

@app.post("/vision")
async def vision(file: UploadFile = File(...), prompt: str = Form("")):
    try:
        contents = await file.read()
        mime_type = file.content_type
        
        vision_instruction = (
            "Look at this image. If it is related to sports, answer the prompt. "
            "If it is off-topic (food, pets, landscapes, fashion, etc.), return exactly: "
            "'This image doesn't appear to be related to sports. Try uploading a game photo, athlete, or sports equipment.'"
        )
        
        prompt_parts = [
            {"mime_type": mime_type, "data": contents},
            vision_instruction + "\\n\\nPrompt: " + prompt
        ]
        
        response = model.generate_content(prompt_parts)
        return {"reply": response.text}
        
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "ResourceExhausted" in error_msg:
            await asyncio.sleep(2)
            try:
                prompt_parts = [
                    {"mime_type": mime_type, "data": contents},
                    vision_instruction + "\\n\\nPrompt: " + prompt
                ]
                response = model.generate_content(prompt_parts)
                return {"reply": response.text}
            except Exception:
                return JSONResponse(status_code=429, content={"reply": "SportsBot is busy right now — try again in a moment."})
        elif "403" in error_msg or "PermissionDenied" in error_msg or "API_KEY_INVALID" in error_msg:
            return JSONResponse(status_code=403, content={"reply": f"API error: {error_msg}"})
        else:
            print(f"Error: {e}")
            return JSONResponse(status_code=500, content={"reply": "Something went wrong — please retry."})
