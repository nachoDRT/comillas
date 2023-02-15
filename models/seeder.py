from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQALCHEMY_DATABASE_URL_ALUMNOS="sqlite:///./students.db"

engine = create_engine(SQALCHEMY_DATABASE_URL_ALUMNOS, connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel = declarative_base()