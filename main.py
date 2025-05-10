from database import Base, engine, SessionLocal
from fastapi import FastAPI, Request, Form, Depends, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Produto
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="tVKo}XRfsfR(dsJ,s?4)Oezrj`3AH[")


# Cria as tabelas no banco (se não existirem ainda)
Base.metadata.create_all(bind=engine)

# Arquivos estáticos (css, js, imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates HTML
templates = Jinja2Templates(directory="templates")

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Página inicial
@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "produtos": produtos
    })

# Adicionar produto
@app.post("/produtos")
def adicionar_produto(
    nome: str = Form(...),
    preco: float = Form(...),
    db: Session = Depends(get_db)
):
    novo_produto = Produto(nome=nome, preco=preco)
    db.add(novo_produto)
    db.commit()
    return RedirectResponse(url="/", status_code=303)


@app.post("/produtos/{produto_id}/remover")
def remover_produto(
    produto_id: int = Path(...),
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
    return RedirectResponse(url="/", status_code=303)
