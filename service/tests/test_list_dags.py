from unittest import TestCase
from os import execvp


class TestListDags(TestCase):
    
    def test1(self):
        #TODO: initialize database before tests.
        execvp('.venv/bin/airflow', ['dags', 'list'])