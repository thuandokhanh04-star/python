from sqlalchemy import Integer,String,Boolean,DateTime,func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import datetime

class User(Base):
    __tablename__ ="users"
    id:Mapped[int] = mapped_column (Integer, primary_key= True,)
    fullname:Mapped[str] = mapped_column(String(100),nullable=False,)
    email:Mapped[str]= mapped_column(String(100),nullable=False,unique=True ,)
    password_hash:Mapped[str]= mapped_column(String(255), nullable=False,)
    is_active:Mapped[bool]=mapped_column(Boolean,nullable=False, default=True,)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


    


