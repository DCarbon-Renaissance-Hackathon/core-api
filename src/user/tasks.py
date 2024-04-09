import logging

logger = logging.getLogger(__name__)

from src import worker


@worker.task_manage.task(name="task_name")
def task_name(data):
    return {"status": 1, "result": "oke"}

