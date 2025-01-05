import dotenv
from pydantic import BaseModel

config = dotenv.dotenv_values(".env")

class Settings(BaseModel):
    SECRET_KEY: str = config["SECRET_KEY"]
    ALGORITHM: str = config["ALGORITHM"]
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config["ACCESS_TOKEN_EXPIRE_MINUTES"]
    TOKEN_TYPE: str = config["TOKEN_TYPE"]
    API_V1_STR: str = config["API_V1_STR"]

    class CONFIG:
        case_sensitive = True

settings = Settings()