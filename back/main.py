from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Arquivos estáticos (css, js, imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates HTML
templates = Jinja2Templates(directory="templates")

# Página inicial (renderiza index.html)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    produtos = [
        {"nome": "Teclado", "preco": 299.99},
        {"nome": "Mouse", "preco": 199.999},
        {"nome": "Oculos Preto de Sol", "preco": 12.99},
        {"nome": "Teclado", "preco": 299.99},
        {"nome": "Mouse", "preco": 199.999},
        {"nome": "Oculos Preto de Sol", "preco": 12.99}
    ]

    return templates.TemplateResponse("index.html", {
    "request": request,
    "produtos": produtos
})
