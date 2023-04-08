from sqlalchemy import Column, Integer, ForeignKey, create_engine

from configs import Base


class Order(Base):
    __tablename__ = "Order"

    id = Column(Integer(), primary_key=True)
    name_type = Column(ForeignKey("Type.id"))
    name_frame_material = Column(ForeignKey("Frame.id"))
    name_frame_colour = Column(ForeignKey("Frame.id"))
    name_casing_material = Column(ForeignKey("CasingMaterials.id"))
    name_cover_material = Column(ForeignKey("Cover.id"))
    name_cover_colour = Column(ForeignKey("Cover.id"))
    furniture = Column(ForeignKey("Furniture.id"))
    country_producer = Column(ForeignKey("Countries.id"))

    def __str__(self):
        return f"Order: {self.id}"

    def __repr__(self):
        return f"Order: {self.id}"
