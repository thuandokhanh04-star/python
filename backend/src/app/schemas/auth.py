from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict
class LoginRequest (BaseModel):
    email:EmailStr
    password: str= Field(min_length=1)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class RegisterRequest(BaseModel):
    fullname: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
    id: int
    fullname: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)