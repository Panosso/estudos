from pydantic import BaseModel

class Settings(BaseModel):
    SECRET_KEY: str = "mysecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class CONFIG:
        case_sensitive = True

settings = Settings()