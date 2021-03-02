import sqlalchemy
# 1.导入path
from settings import path

engine = sqlalchemy.create_engine(path, encoding='utf-8', echo=True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(bind=engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


class BaseModel(Base):
    __abstract__ = True
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    def save(self):
        session.add(self)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

    def update(self):
        session.commit()


class Car(BaseModel):
    __tablename__ = 'car'

    c_name = sqlalchemy.Column(sqlalchemy.String(32))
    c_price = sqlalchemy.Column(sqlalchemy.Integer)
