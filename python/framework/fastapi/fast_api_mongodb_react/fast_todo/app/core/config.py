from typing import List
from decouple import config
from pydantic import AnyHttpUrl, BaseModel

class Settings(BaseModel):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY")
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY")
    ALGORITH: str = "H256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 *7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "TODOFast"

    #Database
    MONGO_CONNECTION_STR: str = config('MONGO_CONNECTION_STR')

    class CONFIG:
        case_sensitive = True

settings = Settings()
