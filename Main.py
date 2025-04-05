from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all CORS (frontend boleh akses)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "XAU/USD AI Backend is running!"}

@app.get("/predict")
def get_prediction():
    import random
    return {
        "action": random.choice(["buy", "sell", "hold"]),
        "confidence": round(random.uniform(0.5, 0.99), 2)
    }
