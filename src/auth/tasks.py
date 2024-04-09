import logging

from src.worker import sync_task

logger = logging.getLogger(__name__)

from src import worker


@worker.task_manage.task(name="task_name")
@sync_task()
async def task_name(data):

    return {"status": 1, "result": "oke"}

