from os import listdir, remove, rmdir
from pathlib import Path
from unittest import TestCase

from .utils import *

DAGS_FOLDER = str(Path('.data/airflow/dags').absolute())


class BasicTestCase(TestCase):

    @staticmethod
    def rmdir(path: Path):
        for file in listdir(path):
            file_path = Path(path, file)
            if file_path.is_dir():
                BasicTestCase.rmdir(file_path)
                rmdir(file_path)
            elif file_path.is_file():
                remove(file_path)
            else:
                raise BaseException(f'Unknown type of entry: {file_path}')

    @classmethod
    def _cleanup_dags_folder(cls):
        # Remove all files in the DAGS_FOLDER
        cls.rmdir(Path(DAGS_FOLDER))

    def _dags_list(self, caller_tag: str):
        stdout_str, stderr_str = execute(f'.venv/bin/airflow dags list', env={
            'AIRFLOW__CORE__DAGS_FOLDER': DAGS_FOLDER,
        })
        real_dags = list(filter(lambda x: DAGS_FOLDER in x, map(
            lambda x: x.strip(), stdout_str.split('\n'))))
        print(f'[{caller_tag},DAGS] {real_dags}')
        print(f'[{caller_tag},STDERR] {stderr_str}')
        return real_dags
