import logging

from fastapi import APIRouter, HTTPException, status

from app.models import schema_send_email
from app.adapters.adapter_send_email import SendEmail

route = APIRouter()


@route.post("/send_email")
def to(schema: schema_send_email.Sender):
    try:
        send_email = SendEmail(schema.to, schema.subject, schema.message)
        result = send_email.send_email()
        if result == "Message sent successfully!":
            return {"message": result}
        else:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=f"Failed to send email: {result}"
            )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Internal server error: {e}"
        )
