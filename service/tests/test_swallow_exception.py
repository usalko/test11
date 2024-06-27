from io import BytesIO
from pathlib import Path

from src.v1 import safety_copy_service

from .basic_test_case import *
from .utils import *

TAG = Path(__file__).name
DAGS_FOLDER = str(Path('.data/airflow/dags').absolute())


class CustomException(BaseException):
    ...


def raise_custom_exception():
    raise CustomException


def testing_function():
    touched_file = '/tmp/file1'
    Path(touched_file).write_text('')
    with open(touched_file, 'r') as r:
        raise_custom_exception()


class TestSwallowException(BasicTestCase):

    def test_not_swallow_exception(self):
        self.assertRaisesRegex(CustomException, '.*', testing_function)
