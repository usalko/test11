from io import open
from os import listdir, remove, rmdir
from pathlib import Path
from subprocess import PIPE, Popen
from typing import Any, Dict, Tuple
from unittest import TestCase

TAG = Path(__file__).name
DAGS_FOLDER = str(Path('.data/airflow/dags').absolute())


HELLO_WORLD_DAG = '''
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('hello_world', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = BashOperator(
    task_id='say_hello',
    bash_command='echo "Hello World from Airflow!"',
    dag=dag,
)
'''


def execute(command: str, env: Dict[str, Any] = {}) -> Tuple[str, str]:
    with Popen(command,
               shell=True,
               text=True,
               stdin=PIPE,
               stdout=PIPE,
               stderr=PIPE,
               bufsize=4096,
               env=env,
               ) as process:
        return process.communicate()


class TestListDags(TestCase):

    @staticmethod
    def rmdir(path: Path):
        for file in listdir(path):
            file_path = Path(path, file)
            if file_path.is_dir():
                TestListDags.rmdir(file_path)
                rmdir(file_path)
            elif file_path.is_file():
                remove(file_path)
            else:
                raise BaseException(f'Unknown type of entry: {file_path}')

    @classmethod
    def _cleanup_dags_folder(cls):
        # Remove all files in the DAGS_FOLDER
        cls.rmdir(Path(DAGS_FOLDER))

    @classmethod
    def setUpClass(cls):
        print(f'[{TAG}] Current value for an absolute path: {
              str(Path(".").absolute())}')

        cls._cleanup_dags_folder()

        stdout_str, stderr_str = execute(f'.venv/bin/airflow db init', env={
            'AIRFLOW__CORE__DAGS_FOLDER': DAGS_FOLDER,
        })
        print(f'[{TAG}] {stdout_str}')
        print(f'[{TAG},STDERR] {stderr_str}')

    def setUp(self) -> None:
        self._cleanup_dags_folder()
        return super().setUp()

    def test_empty_dags_folder(self):
        stdout_str, stderr_str = execute(f'.venv/bin/airflow dags list', env={
            'AIRFLOW__CORE__DAGS_FOLDER': DAGS_FOLDER,
        })
        real_dags = list(filter(lambda x: DAGS_FOLDER in x, map(
            lambda x: x.strip(), stdout_str.split('\n'))))
        print(f'[{TAG},DAGS] {real_dags}')
        print(f'[{TAG},STDERR] {stderr_str}')
        self.assertEqual(len(real_dags), 0)

    def test_simple_dag(self):

        with open(str(Path(DAGS_FOLDER, 'hello_world_dag.py')), 'w') as writer:
            writer.write(HELLO_WORLD_DAG)

        stdout_str, stderr_str = execute(f'.venv/bin/airflow dags list', env={
            'AIRFLOW__CORE__DAGS_FOLDER': DAGS_FOLDER,
        })
        real_dags = list(filter(lambda x: DAGS_FOLDER in x, map(
            lambda x: x.strip(), stdout_str.split('\n'))))
        print(f'[{TAG},DAGS] {real_dags}')
        print(f'[{TAG},STDERR] {stderr_str}')
        self.assertEqual(len(real_dags), 1)
