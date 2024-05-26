from unittest import TestCase
from os import execvp


class TestListDags(TestCase):
    
    def test1(self):
        execvp('airflow dags --list')