from database import Base, engine, SessionLocal
from fastapi import FastAPI, Request, Form, Depends, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Produto
from starlette.middleware.sessions import SessionMiddleware
from starlette.status import HTTP_303_SEE_OTHER

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
    usuario = request.session.get("usuario")
    tipo = request.session.get("tipo")
    return templates.TemplateResponse("index.html", {
        "request": request,
        "produtos": produtos,
        "usuario": usuario,
        "tipo": tipo
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

# Remover produto
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

# Página de login
@app.get("/login")
def show_login(request: Request):
    # Se já estiver logado, redireciona direto
    if request.session.get("usuario") == "adm":
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("login.html", {"request": request})

# Processa o login
@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Dicionário de usuários simples
    usuarios = {
        "adm": {"senha": "123", "tipo": "admin"},
        "cliente": {"senha": "123", "tipo": "cliente"},
    }

    usuario = usuarios.get(username)
    if usuario and usuario["senha"] == password:
        request.session["usuario"] = username
        request.session["tipo"] = usuario["tipo"]
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "Credenciais inválidas"
    })

# Logout
@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

@app.get("/profile", response_class=HTMLResponse)
def perfil(request: Request):
    usuario = request.session.get("usuario")
    tipo = request.session.get("tipo") 

    return templates.TemplateResponse("profile.html", {
        "request": request,
        "usuario": usuario,
        "tipo": tipo or "usuário"
    })


# Página de about
@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    usuario = request.session.get("usuario")
    tipo = request.session.get("tipo")
    
    return templates.TemplateResponse("about.html", {
        "request": request,
        "usuario": usuario,
        "tipo": tipo or "usuário"
    })
