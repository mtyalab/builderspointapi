from datetime import datetime, timedelta
from pydantic import BaseModel


class ResetPasswordRequest(BaseModel):
    email: str
    code: str
    created_at: datetime = datetime.now()


class ResetPasswordConfirm(BaseModel):
    email: str
    code: str
    new_password: str
    created_at: datetime = datetime.now()

    @property
    def is_expired(self):
        return datetime.now() > self.created_at + timedelta(minutes=15)
