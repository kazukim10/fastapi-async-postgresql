from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Item(Base):

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(255), nullable=False)