from pydantic import BaseModel, EmailStr


class SenderBase(BaseModel):
    to: EmailStr


class Sender(SenderBase):
    subject: str
    message: str
