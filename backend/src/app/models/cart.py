from sqlalchemy import (ForeignKey, Integer, UniqueConstraint)
from  sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
class Cart (Base):
    __tablename__="carts"
    id:Mapped[int]=mapped_column(Integer, primary_key=True,)
    user_id:Mapped[int]= mapped_column( ForeignKey("users.id",ondelete="CASCADE"), nullable=False, unique=True, index=True,)
class CartItem(Base):
    __tablename__="cart_items"
    __table_args__=(UniqueConstraint("cart_id","product_id",name="uq_cart_items_cart_products",),)
    id:Mapped [int]=mapped_column(Integer, primary_key=True,)
    cart_id:Mapped[int]=mapped_column( ForeignKey("carts.id",ondelete="CASCADE"),nullable=False,)
    product_id:Mapped[int]=mapped_column(ForeignKey("products.id",ondelete="RESTRICT"),nullable=False,)
    quantity:Mapped[int]=mapped_column(Integer, nullable=False, default=1),

