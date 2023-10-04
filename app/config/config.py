
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import EmailStr

load_dotenv()


class RootUserEmail(BaseSettings):
    email: EmailStr
    password: str

    class Config:
        env_file = "../../.env"
        env_file_encoding = 'utf-8'
