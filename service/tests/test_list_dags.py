from os import _wrap_close
from subprocess import PIPE, Popen
from typing import Any, Dict
from unittest import TestCase


def popen(command: str, env: Dict[str, Any] = {}):
    proc = Popen(command,
                 shell=True,
                 text=True,
                 stdin=PIPE,
                 bufsize=4096,
                 )
    return _wrap_close(proc.stdin, proc)  # type: ignore


class TestListDags(TestCase):

    def test1(self):
        # TODO: initialize database before tests.
        # p = os.popen("ps -eo pid,ppid,args")
        # output = p.read()
        # p.close()

        with popen(f'.venv/bin/airflow db init', env={}) as process:
            print(process.read())

        with popen(f'.venv/bin/airflow dags list') as process:
            dags_list_result = process.read()
        self.assertIsNotNone(dags_list_result)
