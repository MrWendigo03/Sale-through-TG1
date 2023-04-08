from sqlalchemy import Column, Integer, String

from models.models import Base

class Sales(Base):
    __tablename__ = "Special sales"

    id = Column(Integer(), primary_key=True)
    name_of_sale = Column(String(64), nullable=False)
    description = Column(String(1024), nullable=False)

    def __str__(self):
        return f"Special sales: {self.id}"

    def __repr__(self):
        return f"Special sales: {self.id}"