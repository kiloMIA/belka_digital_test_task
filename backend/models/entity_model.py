from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)


class ReportDB(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    month = Column(String)
    raw_material = Column(String)
    content_of_iron = Column(Float)
    content_of_sulfur = Column(Float)
    content_of_silicon = Column(Float)
    content_of_calcium = Column(Float)
    content_of_aluminum = Column(Float)