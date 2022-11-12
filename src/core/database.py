from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import config


SQLALCHEMY_DATABASE_URL = 'postgresql+pg8000://{0}:{1}@{2}:{3}/{4}'.format(
    config.POSTGRES_USER,
    config.POSTGRES_PASSWORD,
    config.UVICORN_HOST,
    5432,
    config.POSTGRES_DB
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
