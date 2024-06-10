from io import BytesIO
from shutil import copyfile
from typing import List

from ....common import *
from ..schemas import *
from pathlib import Path

SAFETY_COPY_BUFFER_SIZE = 4096


def safety_copy(*, tmp_folder: str, target_folder: str, stream: BytesIO, file_name: str) -> bool:
    '''Safety copy or rollback folder content.'''
    target_file_name = Path(target_folder, f'{file_name}')

    if not target_file_name.exists():
        # Case 1 no named file in the target folder
        tmp_file_name = Path(tmp_folder, f'{file_name}')
        with open(tmp_file_name, 'wb') as writer:
            chunk = stream.read(SAFETY_COPY_BUFFER_SIZE)
            while chunk:
                writer.write(chunk)
                chunk = stream.read(SAFETY_COPY_BUFFER_SIZE)

        copyfile(tmp_file_name, target_file_name)

    else:
        # Case 2 target folder contains file within the same name

        # Backup existing file
        backup_file_name = Path(tmp_folder, f'{file_name}.bak')
        copyfile(target_file_name, backup_file_name)

        tmp_file_name = Path(tmp_folder, f'{file_name}')
        with open(tmp_file_name, 'wb') as writer:
            chunk = stream.read(SAFETY_COPY_BUFFER_SIZE)
            while chunk:
                writer.write(chunk)
                chunk = stream.read(SAFETY_COPY_BUFFER_SIZE)

        copyfile(tmp_file_name, target_file_name)

    return True
