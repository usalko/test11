from subprocess import PIPE, Popen
from typing import Any, Dict, Tuple


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
