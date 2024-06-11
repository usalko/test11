from io import BytesIO
from os import remove
from pathlib import Path
from shutil import copyfile, move
from typing import List

from ....common import *
from ..schemas import *

SAFETY_COPY_BUFFER_SIZE = 4096
SAFETY_COPY_HEALTH_CHECK_TIMEOUT = 300


def _check_airflow_healthy_condition(health_check_timeout: float) -> bool:
    return True


def safety_copy_service(*, tmp_folder: str, target_folder: str, stream: BytesIO, file_name: str) -> bool:
    '''Safety copy or rollback folder content.'''
    target_file_name = Path(target_folder, f'{file_name}')

    tmp_file_name = Path(tmp_folder, f'{file_name}')
    with open(tmp_file_name, 'wb') as writer:
        chunk = stream.read(SAFETY_COPY_BUFFER_SIZE)
        while chunk:
            writer.write(chunk)
            chunk = stream.read(SAFETY_COPY_BUFFER_SIZE)
    try:
        if not target_file_name.exists():
            # Case 1 no named file in the target folder
            backup_file_name = None

        else:
            # Case 2 target folder contains file within the same name

            # Backup existing file
            backup_file_name = Path(tmp_folder, f'{file_name}.bak')
            move(target_file_name, backup_file_name)

        copyfile(tmp_file_name, target_file_name)

        if _check_airflow_healthy_condition(SAFETY_COPY_HEALTH_CHECK_TIMEOUT):
            return True

        # Rollback folder state
        if backup_file_name:
            move(backup_file_name, target_file_name)
        else:
            remove(target_file_name)
    finally:
        remove(tmp_file_name)

    return False
