from typing import Annotated

from fastapi import Depends

from .db_session import DbSession
from .schemas import *


def common_parameters(
    current_user: AirflowUser,
    db_session: DbSession,
):
    return {
        'db_session': db_session,
        'current_user': current_user,
    }


CommonParameters = Annotated[
    dict[str, int | AirflowUser | DbSession],
    Depends(common_parameters),
]
