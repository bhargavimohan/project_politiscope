from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Date,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


Base = declarative_base()

DATABASE_URL = "sqlite:///../politiscope_database/politiscope.db"
#DATABASE_URL = "sqlite:///DB/esa_dev.db"

engine = create_engine(DATABASE_URL, echo=False)
# Creating a scoped session factory
Session = scoped_session(sessionmaker(bind=engine))


class MainCategory(Base):
    __tablename__ = 't_users' 

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(collation='NOCASE'))
    email = Column(String(collation='NOCASE'), unique=True, index=True)
    password = Column(String)