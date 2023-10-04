from fastapi import FastAPI
from app.endpoints.router_send_email import route as send_email_route

app = FastAPI()

app.include_router(send_email_route)
