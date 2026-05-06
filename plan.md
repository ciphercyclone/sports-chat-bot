# Implementation Plan — SportsBot

## Stack
| Layer | Technology |
|---|---|
| Backend | FastAPI (Python 3.11+) |
| AI Model | `gemini-2.5-flash-lite` via `google-generativeai` Python SDK |
| Frontend | Vanilla JS + Tailwind CSS (existing `code.html` — do not modify structure) |
| Markdown Rendering | `marked.js` via CDN, injected into `code.html` |
| Config | `python-dotenv` — `GEMINI_API_KEY` loaded from `.env` |
| Server | `uvicorn`, port `8000` |

---

## Project Structure
```
sportsbot/
├── main.py            # FastAPI app — all routes
├── .env               # GEMINI_API_KEY=your_key_here (not committed)
├── requirements.txt   # Dependencies
└── static/
    └── code.html      # UI (copied from export, lightly modified)
```

---

## Components — Build Order

### 1. Environment & Dependencies
- `requirements.txt`: `fastapi`, `uvicorn`, `google-generativeai`, `python-dotenv`, `python-multipart`
- `.env` file with `GEMINI_API_KEY`
- Load key at startup with `python-dotenv`

### 2. FastAPI App Bootstrap (`main.py`)
- Initialize app
- Mount `static/` directory
- Serve `static/code.html` at `GET /`
- Load Gemini client once at startup using `genai.configure(api_key=...)`

### 3. System Instruction
Define as a module-level constant. Sports-scoped, helpful, non-paranoid. Include explicit instruction to use Markdown formatting in responses.

### 4. `/chat` POST Endpoint
- Request body: `{ "message": str, "history": list[dict] }`
- Build `ChatSession` with full history + system instruction
- Call `model.generate_content()`
- Return: `{ "reply": str }`
- Error handling: 429 with backoff, 403/GoogleAPIError with real message, generic fallback

### 5. `/vision` POST Endpoint
- Accepts multipart: `file: UploadFile`, `prompt: str` (optional)
- Read image bytes, encode to base64, pass inline to Gemini multimodal call
- Include topic-verification instruction in the prompt
- Return: `{ "reply": str }`
- Same error handling as `/chat`

### 6. Frontend Wiring (`code.html` modifications)
All changes are additive JS — the HTML structure is preserved.

#### 6a. Add `marked.js` CDN
```html
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
```

#### 6b. Empty-Send Guard
- On `textarea` `input` event: if `value.trim() === ''`, disable Send button (add `opacity-50 cursor-not-allowed`, remove click handler or set disabled).
- On non-empty input: enable Send button.
- Guard also on Enter key handler.

#### 6c. Chat State & DOM Management
- Track `conversationHistory` array in JS.
- On first message sent: hide empty state (`<main>` with chips), show `<div id="chat-list">` instead.
- `appendMessage(role, htmlContent)`: creates bubble, inserts into chat list, scrolls to bottom.

#### 6d. Send Handler
- Collect `textarea` value.
- Push to `conversationHistory` as `{ role: "user", parts: [{ text }] }`.
- Append user bubble immediately.
- POST to `/chat` with message + history.
- On response: render reply through `marked.parse()`, append bot bubble.
- On error: append error bubble with message from backend.

#### 6e. Image Upload Handler
- On attachment button click: trigger hidden `<input type="file" accept="image/*">`.
- On file selected: show preview thumbnail in input area.
- On send: POST to `/vision` as `multipart/form-data` with file + textarea text.
- Clear preview after send.

#### 6f. Suggestion Chip Wiring
- Each chip `onclick`: set `textarea.value` to chip text, trigger send handler.

---

## API Reference
- SDK docs: https://ai.google.dev/gemini-api/docs
- Model: `gemini-2.5-flash-lite`
- Free tier: 15 RPM, 1,000 RPD, 1M token context, multimodal supported

---

## Running the App
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
# Open http://localhost:8000
```
