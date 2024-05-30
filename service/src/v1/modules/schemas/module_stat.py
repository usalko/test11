from datetime import datetime

from pydantic import BaseModel


class ModuleStat(BaseModel):
    name: str
    description: str
    stamp: datetime