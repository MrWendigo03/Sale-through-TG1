from typing import Any

import sqlalchemy as db

from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from models.order import Order
from configs import Base, engine


@dataclass
class DataBase:
    HOST: str
    USER: str
    PASSWORD: str
    DB_USER: str


class FrameInfo(Base):
    __tablename__ = "Frame"

    id = Column(Integer(), primary_key=True)
    name_frame_material = Column(String(64), unique=True, nullable=False)
    name_frame_colour = Column(String(16), unique=True, nullable=False)

    def __str__(self):
        return f"Frame: {self.id}"

    def __repr__(self):
        return f"Frame: {self.id}"


class CasingMaterial(Base):
    __tablename__ = "CasingMaterials"

    id = Column(Integer(), primary_key=True)
    name_casing_material = Column(String(32), unique=True, nullable=False)

    def __str__(self):
        return f"CasingMaterials: {self.id}"

    def __repr__(self):
        return f"CasingMaterials: {self.id}"


class CoverInfo(Base):
    __tablename__ = "Cover"

    id = Column(Integer(), primary_key=True)
    name_cover_material = Column(String(32), unique=True, nullable=False)
    name_cover_colour = Column(String(16), unique=True, nullable=False)

    def __str__(self):
        return f"Cover: {self.id}"

    def __repr__(self):
        return f"Cover: {self.id}"


class FurnitureInfo(Base):
    __tablename__ = "Furniture"

    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return f"Furniture: {self.id}"

    def __repr__(self):
        return f"Furniture: {self.id}"


class CountryInfo(Base):
    __tablename__ = "Countries"

    id = Column(Integer(), primary_key=True)
    country_name = Column(String(64), nullable=False)

    def __str__(self):
        return f"Countries: {self.id}"

    def __repr__(self):
        return f"Countries: {self.id}"
