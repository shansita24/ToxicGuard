# ToxicGuard 🔥

Real-time Instagram toxicity detection using NLP.

## Features
- Detects abusive comments/messages
- Hinglish + English support
- Chrome extension + FastAPI backend
- Transformer-based model (toxic-bert)

## Tech Stack
- FastAPI
- Transformers (HuggingFace)
- Chrome Extension (JS)
- PyTorch

## Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload


Extension
Go to chrome://extensions
Enable Developer Mode
Load unpacked → select extension/
API

http://127.0.0.1:8000/docs