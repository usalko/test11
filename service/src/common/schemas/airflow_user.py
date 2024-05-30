from pydantic import BaseModel


class AirflowUser(BaseModel):
    login: str