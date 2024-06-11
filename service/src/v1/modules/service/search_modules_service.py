from ....common import *
from ..schemas import *
from typing import List


def search_modules_service(*, db_session: DbSession, module_id: int) -> List[ModuleStat]:
    '''Returns all modules.'''
    if module_id:
        # return db_session.query(CostModel).filter(CostModel.project_id == project_id)
        raise BaseException('Not implemented')
    return []  # db_session.query(ModuleStat)
