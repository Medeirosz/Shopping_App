from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API FastAPI no ar!"}