from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Cria o banco localmente
DATABASE_URL = "sqlite:///./produtos.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
    