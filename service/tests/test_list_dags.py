from unittest import TestCase
from os import execvp


class TestListDags(TestCase):

    def test1(self):
        # TODO: initialize database before tests.
        # p = os.popen("ps -eo pid,ppid,args")
        # output = p.read()
        # p.close()
        execvp('.venv/bin/airflow', ['dags', 'list'])
