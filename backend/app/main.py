from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import TextRequest, BatchRequest
from .model import predict, batch_predict
from .utils import validate_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # IMPORTANT for extension
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "running"}


@app.post("/predict")
def classify(req: TextRequest):
    if not validate_text(req.text):
        raise HTTPException(status_code=400, detail="Invalid input")

    return predict(req.text)


@app.post("/batch")
def classify_batch(req: BatchRequest):
    if len(req.texts) > 50:
        raise HTTPException(status_code=400, detail="Too many inputs")

    return batch_predict(req.texts)