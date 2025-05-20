from database import Base, engine, SessionLocal
from fastapi import FastAPI, Request, Form, Depends, Path, HTTPException, status
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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def admin_required(request: Request):
    if request.session.get("tipo") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Somente administradores")


def get_current_user(request: Request) -> int:
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login necessário")
    return user_id


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()
    usuario  = request.session.get("usuario")
    tipo     = request.session.get("tipo")
    try:
        user_id = get_current_user(request)
        carrinho = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    except HTTPException:
        carrinho = []

    return templates.TemplateResponse("index.html", {
        "request":  request,
        "produtos": produtos,
        "usuario":  usuario,
        "tipo":     tipo,
        "carrinho": carrinho
    })


@app.post("/produtos", dependencies=[Depends(admin_required)])
def adicionar_produto(
    nome: str = Form(...),
    preco: float = Form(...),
    db: Session = Depends(get_db)
):
    novo = Produto(nome=nome, preco=preco)
    db.add(novo)
    db.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


@app.post("/produtos/{produto_id}/remover", dependencies=[Depends(admin_required)])
def remover_produto(
    produto_id: int = Path(...),
    db: Session = Depends(get_db)
):
    produto = db.get(Produto, produto_id)
    if produto:
        db.delete(produto)
        db.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


@app.get("/login", response_class=HTMLResponse)
def show_login(request: Request):
    if request.session.get("usuario"):
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Aqui você substituiria pelo seu lookup real no DB
    usuarios = {
        "adm":     {"senha": "123", "tipo": "admin",   "id": 1},
        "cliente": {"senha": "123", "tipo": "cliente", "id": 2},
    }
    user = usuarios.get(username)
    if user and user["senha"] == password:
        request.session["usuario"] = username
        request.session["tipo"]    = user["tipo"]
        request.session["user_id"] = user["id"]
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

    return templates.TemplateResponse("login.html", {
        "request": request,
        "error":   "Credenciais inválidas"
    })


@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


@app.get("/profile", response_class=HTMLResponse)
def profile(request: Request, db: Session = Depends(get_db)):
    user_id  = get_current_user(request)
    carrinho = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    return templates.TemplateResponse("profile.html", {
        "request":  request,
        "usuario":  request.session.get("usuario"),
        "tipo":     request.session.get("tipo"),
        "carrinho": carrinho
    })


@app.get("/about", response_class=HTMLResponse)
def about(request: Request, db: Session = Depends(get_db)):
    try:
        user_id = get_current_user(request)
        carrinho = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    except HTTPException:
        carrinho = []
    return templates.TemplateResponse("about.html", {
        "request":  request,
        "usuario":  request.session.get("usuario"),
        "tipo":     request.session.get("tipo"),
        "carrinho": carrinho
    })


@app.post("/carrinho/adicionar")
def add_to_cart(
    request: Request,
    produto_id: int = Form(...),
    db: Session = Depends(get_db)
):
    user_id = get_current_user(request)
    produto = db.get(Produto, produto_id)
    if produto:
        item = CartItem(user_id=user_id, nome=produto.nome, preco=produto.preco)
        db.add(item)
        db.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


@app.post("/carrinho/limpar")
def clear_cart(request: Request, db: Session = Depends(get_db)):
    user_id = get_current_user(request)
    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    db.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


@app.post("/carrinho/remover/{item_id}")
def remover_item_carrinho(
    request: Request,
    item_id: int,
    db: Session = Depends(get_db)
):
    user_id = get_current_user(request)
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == user_id
    ).first()
    if item:
        db.delete(item)
        db.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)


@app.post("/produtos/{produto_id}/editar", dependencies=[Depends(admin_required)])
def editar_produto(
    produto_id: int = Path(...),
    nome: str = Form(...),
    preco: float = Form(...),
    db: Session = Depends(get_db)
):
    produto = db.get(Produto, produto_id)
    if produto:
        produto.nome  = nome
        produto.preco = preco
        db.commit()
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
