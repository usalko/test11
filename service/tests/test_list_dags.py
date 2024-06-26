from io import open
from pathlib import Path

from .basic_test_case import BasicTestCase
from .utils import *

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


class TestListDags(BasicTestCase):

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
        real_dags = self._dags_list(TAG)
        self.assertEqual(len(real_dags), 0)

    def test_simple_dag(self):

        with open(str(Path(DAGS_FOLDER, 'hello_world_dag.py')), 'w') as writer:
            writer.write(HELLO_WORLD_DAG)

        real_dags = self._dags_list(TAG)
        self.assertEqual(len(real_dags), 1)
