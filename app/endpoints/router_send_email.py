import logging
from fastapi import APIRouter, HTTPException, status

from app.models import schema_send_email
from app.adapters.adapter_send_email import SendEmail

route = APIRouter()
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")


@route.post("/send_email")
def to(schema: schema_send_email.Sender):
    try:
        send_email = SendEmail(schema.to, schema.subject, schema.message)
        result = send_email.send_email()
        if result == "Message sent successfully!":
            logging.info(f"Message sent successfully to {schema.to}")
            return {"message": result}
        else:
            logging.warning(f"Failed to send email to {schema.to}: {result}")
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=f"Failed to send email: {result}"
            )

    except Exception as e:
        logging.error(f"Internal server error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error"
        )
