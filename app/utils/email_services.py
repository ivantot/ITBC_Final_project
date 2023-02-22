"""Utils module."""
import asyncio
from fastapi_mail import ConnectionConfig, MessageSchema, MessageType, FastMail

from app.config import settings


class EmailServices:
    """EmailServices class"""
    conf = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
    )

    @staticmethod
    def send_money_account_warning_email(email: str, balance: float, amount: float,
                                         user: str, transaction_currency: str, vendor_name: str,
                                         money_account_currency: str):
        """send_money_account_warning_email function"""
        html = f"""<p>Dear service user {user} </p>
        <p>Transaction you're attempting at {vendor_name} did not succeed, as the transaction amount is <b>{amount}</b>
         {transaction_currency} and you have <b>{balance}</b> {money_account_currency} available 
         on your money account.</p><p>Sorry for the inconvenience. Enjoy your day.</p>"""

        message = MessageSchema(
            subject="Not enough funds to complete the transaction.",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(EmailServices.conf)
        asyncio.run(fm.send_message(message))

        return
