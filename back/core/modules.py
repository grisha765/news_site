from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    user: str
    role: str

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")

