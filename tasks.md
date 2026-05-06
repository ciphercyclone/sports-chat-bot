# Build Tasks — SportsBot

## Task 1 — Scaffold project structure
Create the project folder with `main.py`, `requirements.txt`, `.env`, and a `static/` subfolder. Copy `code.html` into `static/`.

## Task 2 — Write `requirements.txt` and install dependencies
Add `fastapi`, `uvicorn[standard]`, `google-generativeai`, `python-dotenv`, and `python-multipart`. Run `pip install -r requirements.txt`.

## Task 3 — Load `GEMINI_API_KEY` from `.env`
In `main.py`, use `python-dotenv` to load `.env` at startup and call `genai.configure(api_key=os.getenv("GEMINI_API_KEY"))`. If the key is missing, raise a clear startup error.

## Task 4 — Create the FastAPI app, serve `code.html` at `/`
Initialize the FastAPI app, mount the `static/` directory, and add a `GET /` route that returns `code.html` via `FileResponse`.

## Task 5 — Define the system instruction constant
Write a module-level `SYSTEM_INSTRUCTION` string that scopes the bot to sports, instructs it to be helpful and non-paranoid, permits general sports knowledge with disclaimers, and tells it to format responses in Markdown.

## Task 6 — Build the `/chat` POST endpoint
Accept `{ "message": str, "history": list }`, build a Gemini chat session with the system instruction and full history, call `generate_content`, and return `{ "reply": str }`.

## Task 7 — Build the `/vision` POST endpoint
Accept `multipart/form-data` with an image file and optional text prompt. Read the image bytes, pass them inline to Gemini's multimodal model alongside the prompt and a topic-verification instruction, and return `{ "reply": str }`.

## Task 8 — Add error handling to both endpoints (429, 403, generic)
For HTTP 429, retry once after a 2-second `asyncio.sleep`; if still failing, return `{ "reply": "SportsBot is busy right now — try again in a moment." }`. For HTTP 403, `PermissionDenied`, or any `GoogleAPIError`, return `{ "reply": f"API error: {str(e)}" }` — never swallow this as a generic message. For all other exceptions, log them and return `{ "reply": "Something went wrong — please retry." }`.

## Task 9 — Remove all demo/placeholder content from `code.html`
Delete any hardcoded sample messages, fake chat history, demo bot replies, or placeholder conversations in `code.html`. The chat list must be empty on load; only real API responses should appear.

## Task 10 — Add `marked.js` and wire Markdown rendering
Add `<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>` to `code.html`. Wherever bot reply text is inserted into the DOM, wrap it with `marked.parse(replyText)` and set via `innerHTML` so `**bold**`, `*italics*`, and lists render as proper HTML — never as raw symbols.

## Task 11 — Implement the empty-send guard
On the `textarea`'s `input` event, check `textarea.value.trim() === ''`. If empty, disable the Send button (set `disabled = true`, apply `opacity-50 cursor-not-allowed` classes, remove the active green style). Re-enable it when the value is non-empty. Apply the same guard on the Enter key handler so pressing Enter on an empty field does nothing.

## Task 12 — Wire suggestion chips to the chat
Add `onclick` handlers to all three suggestion chips in `code.html`. Each click should: set `textarea.value` to the chip's question text, trigger the empty-send guard to enable the button, and call the send handler to submit immediately.

## Task 13 — Implement image upload flow
Add a hidden `<input type="file" accept="image/*">` triggered by the attachment (paperclip) button. On file selection, show a small thumbnail preview in the input bar. On send, POST to `/vision` as `multipart/form-data` with the file and any text in the textarea; clear the preview afterward. If no file is selected, use the `/chat` endpoint as normal.

## Task 14 — Test end-to-end and verify all requirements
Confirm: (a) sports questions return Markdown-rendered answers; (b) off-topic images return the redirect message; (c) empty sends are blocked; (d) a bad API key shows the real error message in chat; (e) the app starts cleanly with `uvicorn main:app --reload --port 8000` and opens at `http://localhost:8000`.
