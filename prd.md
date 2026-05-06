# Product Requirements Document — SportsBot

## Vision
SportsBot is a mobile-first, topic-specialized AI chatbot that answers sports questions conversationally. It acts as a knowledgeable "sideline reporter" — confident, friendly, and fast — powered by Gemini and delivered through a clean green-and-white UI.

## Target User
Sports fans of all levels who want quick, reliable answers about scores, rules, players, tactics, and history — primarily on mobile, via a browser-based chat interface.

---

## Must-Have Features

### 1. Sports-Specialized Chat (`/chat`)
- Accept a text message and return a Gemini-generated response scoped to sports topics.
- Maintain conversational context across the session (multi-turn history passed per request).
- Render bot responses as formatted Markdown (bold, italics, lists) — never raw `**` or `*` symbols.
- Block empty or whitespace-only sends at the frontend (Send button disabled).

### 2. Image Upload with Topic Verification (`/vision`)
- Accept an image upload alongside an optional text prompt.
- Pass both to Gemini's multimodal endpoint.
- If the image is sports-related, answer the question.
- If the image is off-topic (food, pets, landscapes, fashion, etc.), return a friendly redirect: *"This image doesn't appear to be related to sports. Try uploading a game photo, athlete, or sports equipment."*

### 3. System Instruction — Helpful, Not Paranoid
The bot **must** answer general sports questions, including well-established rules, historical records, player comparisons, and tactical analysis — **with appropriate disclaimers when relevant** (e.g., predictions, injury speculation).

The bot **must refuse only**:
- Requests completely unrelated to sports (politics, finance, cooking, etc.)
- Harmful or abusive requests
- Content that is inappropriate regardless of domain

The bot **must NOT refuse** routine sports questions by being overly cautious.

### 4. Error Handling (User-Visible)
| Error | Behavior |
|---|---|
| HTTP 429 (rate limit) | Retry once after 2s. If still failing, show: *"SportsBot is busy right now — try again in a moment."* |
| HTTP 403 / PermissionDenied / GoogleAPIError | Show actual error in chat (e.g., *"API key is invalid or has no permissions for this project"*) to aid debugging. |
| Other exceptions | Log server-side, show: *"Something went wrong — please retry."* |

### 5. UI — Use Existing HTML As-Is
- `code.html` is the sole frontend file. Do not redesign it.
- Serve it at `/` from the FastAPI backend.
- Wire suggestion chips to pre-fill and submit the input field.
- Hide empty state and show chat messages once conversation begins.

---

## Non-Goals
- No user authentication or accounts.
- No persistent conversation history (session only).
- No sports data APIs or live score feeds (Gemini's knowledge only).
- No dark mode toggle in v1.
- No admin dashboard or analytics.

---

## Success Criteria
- User can send a sports question and receive a Markdown-rendered response in under 5 seconds on a standard connection.
- Image uploads are correctly routed — sports images answered, off-topic images politely redirected.
- Empty messages cannot be sent.
- Rate limit and auth errors surface clearly in the chat UI.
- App runs on `http://localhost:8000` with a single `uvicorn` command.
