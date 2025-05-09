from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (pode ser removido se front estiver 100% dentro do back)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Arquivos estáticos (css, js, imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates HTML
templates = Jinja2Templates(directory="templates")

# Página inicial (renderiza index.html)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    produtos = [
        {"nome": "Teclado", "preco": 299.99},
        {"nome": "Mouse", "preco": 199.999}
    ]

    return templates.TemplateResponse("index.html", {
    "request": request,
    "produtos": produtos
})



# @app.get("/produtos", response_class=HTMLResponse)
# def produtos(request: Request):

#     produtos = [
#         {"nome": "Camiseta", "preco": 89.90},
#         {"nome": "Tênis", "preco": 219.99},
#     ]

#     return produtos