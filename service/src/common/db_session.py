from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.requests import Request


def get_db(request: Request):
    return request.state.db


DbSession = Annotated[Session, Depends(get_db)]
