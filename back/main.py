from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],  # só o front pode chamar, Só aceita requisições vindas do front local
    allow_credentials=True, #Permite cookies/sessões se usar login futuramente
    allow_methods=["*"], #Permite GET, POST, PUT, etc
    allow_headers=["*"], #Permite qualquer header necessário, tipo Content-Type: application/json
)

@app.get("/")
def home():
    return {"mensagem": "API FastAPI no ar!"}