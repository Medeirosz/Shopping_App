from database import Base, engine, SessionLocal
from fastapi import FastAPI, Request, Form, Depends, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
from starlette.status import HTTP_303_SEE_OTHER
from models import Produto, CartItem

app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key="tVKo}XRfsfR(dsJ,s?4)Oezrj`3AH["
)

# Cria as tabelas se não existirem
Base.metadata.create_all(bind=engine)

# Monta arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura templates
templates = Jinja2Templates(directory="templates")

# Dependência para sessão do DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    # Lista de produtos
    produtos = db.query(Produto).all()

    # Dados de sessão
    usuario = request.session.get("usuario")
    tipo = request.session.get("tipo")

    # TODO: substituir fallback por user_id real
    user_id = 1
    carrinho = db.query(CartItem).filter(CartItem.user_id == user_id).all()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "produtos": produtos,
        "usuario": usuario,
        "tipo": tipo,
        "carrinho": carrinho
    })


@app.post("/produtos")
def adicionar_produto(
    nome: str = Form(...),
    preco: float = Form(...),
    db: Session = Depends(get_db)
):
    novo = Produto(nome=nome, preco=preco)
    db.add(novo)
    db.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


@app.post("/produtos/{produto_id}/remover")
def remover_produto(
    produto_id: int = Path(...),
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


@app.get("/login", response_class=HTMLResponse)
def show_login(request: Request):
    if request.session.get("usuario") == "adm":
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    usuarios = {
        "adm":     {"senha": "123", "tipo": "admin"},
        "cliente": {"senha": "123", "tipo": "cliente"},
    }
    user = usuarios.get(username)
    if user and user["senha"] == password:
        request.session["usuario"] = username
        request.session["tipo"]    = user["tipo"]
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "Credenciais inválidas"
    })


@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


@app.get("/profile", response_class=HTMLResponse)
def perfil(request: Request):
    return templates.TemplateResponse("profile.html", {
        "request": request,
        "usuario": request.session.get("usuario"),
        "tipo":    request.session.get("tipo") or "usuário"
    })


@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {
        "request": request,
        "usuario": request.session.get("usuario"),
        "tipo":    request.session.get("tipo") or "usuário"
    })


@app.post("/carrinho/adicionar")
def add_to_cart(
    request: Request,
    produto_id: int = Form(...),
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).get(produto_id)
    if produto:
        # TODO: usar user_id real em vez de 1
        user_id = 1
        item = CartItem(
            user_id=user_id,
            nome=produto.nome,
            preco=produto.preco
        )
        db.add(item)
        db.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


@app.post("/carrinho/limpar")
def clear_cart(request: Request, db: Session = Depends(get_db)):
    # TODO: usar user_id real em vez de 1
    user_id = 1
    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    db.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
