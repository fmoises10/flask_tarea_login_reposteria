
from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
    Date,
    ForeignKey
)
from sqlalchemy.orm import relationship


class Categoria(Model):
    __tablename__ = "categoria"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(String(250))
    activo = Column(Boolean, default=True)

    ingredientes = relationship(
        "Ingrediente",
        back_populates="categoria"
    )

    def __repr__(self):
        return self.nombre


class Ingrediente(Model):
    __tablename__ = "ingrediente"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    categoria_id = Column(
        Integer,
        ForeignKey("categoria.id"),
        nullable=False
    )

    categoria = relationship(
        "Categoria",
        back_populates="ingredientes"
    )

    cantidad = Column(Float, nullable=False, default=0)
    unidad_medida = Column(String(50), nullable=False)
    costo_unitario = Column(Float, nullable=False, default=0)
    stock_minimo = Column(Float, nullable=False, default=0)
    fecha_vencimiento = Column(Date)
    activo = Column(Boolean, default=True)

    def __repr__(self):
        return self.nombre
