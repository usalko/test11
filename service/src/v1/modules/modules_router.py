from fastapi import APIRouter
from logging import getLogger
from .schemas import *
from .service import *
from ...common import *

log = getLogger(__name__)

modules_router = APIRouter()


@modules_router.get('', response_model=ModuleStat)
def get_modules(common: CommonParameters):
    '''Get all modules.'''
    return search_modules_service(**common)  # type: ignore
