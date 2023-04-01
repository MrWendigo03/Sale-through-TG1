from typing import Any

import sqlalchemy as db

from dataclasses import dataclass
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session

engine = create_engine("postgresql://postgres:postgres@localhost:5432/transactions")
Base = declarative_base(bind=engine)


@dataclass
class DataBase:
    HOST: str
    USER: str
    PASSWORD: str
    DB_USER: str


class Frame(Base):
    __tablename__ = "Frame"

    id = Column(Integer(), primary_key=True)
    name_frame_material = Column(String(64), unique=True, nullable=False)
    name_frame_colour = Column(String(16), unique=True, nullable=False)

    def __str__(self):
        return f"Frame: {self.id}"

    def __repr__(self):
        return f"Frame: {self.id}"


class CasingMaterials(Base):
    __tablename__ = "CasingMaterials"

    id = Column(Integer(), primary_key=True)
    name_casing_material = Column(String(32), unique=True, nullable=False)

    def __str__(self):
        return f"CasingMaterials: {self.id}"

    def __repr__(self):
        return f"CasingMaterials: {self.id}"


class Cover(Base):
    __tablename__ = "Cover"

    id = Column(Integer(), primary_key=True)
    name_cover_material = Column(String(32), unique=True, nullable=False)
    name_cover_colour = Column(String(16), unique=True, nullable=False)

    def __str__(self):
        return f"Cover: {self.id}"

    def __repr__(self):
        return f"Cover: {self.id}"


class Furniture(Base):
    __tablename__ = "Furniture"

    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return f"Furniture: {self.id}"

    def __repr__(self):
        return f"Furniture: {self.id}"


class Order(Base):
    __tablename__ = "Order"

    id = Column(Integer(), primary_key=True)
    name_frame_material = Column(ForeignKey("Frame.id"))
    name_frame_colour = Column(ForeignKey("Frame.id"))
    name_casing_material = Column(ForeignKey("CasingMaterials.id"))
    name_cover_material = Column(ForeignKey("Cover.id"))
    name_cover_colour = Column(ForeignKey("Cover.id"))
    furniture = Column(ForeignKey("Furniture"))

    def __str__(self):
        return f"Order: {self.id}"

    def __repr__(self):
        return f"Order: {self.id}"


class BaseModel:

    def __init__(self, d_b: DataBase):
        self.session = Session(bind=engine)
        self.engine = db.create_engine(f'postgresql://{d_b.USER}:'
                                       f'{d_b.PASSWORD}@'
                                       f'{d_b.HOST}:5432/'
                                       f'{d_b.DB_USER}')

    def creation_db(self):
        Base.metadata.create_db(self.engine)

    def create_event(
        self, client_type_state: str, client_material_frame_state: str, client_colour_material_frame_state: str,
            client_material_casing_state: str, client_type_material_cover_state: str,
            client_colour_material_cover_state: str, client_country_state: str) -> Column[Any]:
        event = Order(
            c_type=client_type_state, c_frame_mat=client_material_frame_state,
            c_col_mat_frame_state=client_colour_material_frame_state, c_mat_cas_state=client_material_casing_state,
            c_type_mat_cover_state=client_type_material_cover_state,
            c_col_mat_cover_state=client_colour_material_cover_state, c_country_state=client_country_state)
        self.session.add(event)
        self.session.commit()
        return self.session.query(Order).all()[-1].id
