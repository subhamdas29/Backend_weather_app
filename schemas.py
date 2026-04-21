from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str
    home_city: str
class ShowUser(BaseModel):
    username: str
    email: str
    home_city: str

    class Config:
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None