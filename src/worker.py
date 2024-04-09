__import__("os").environ["TZ"] = "UTC"

import sentry_sdk
from celery import Celery
from sentry_sdk.integrations.celery import CeleryIntegration

from src.config import settings
import asyncio
import functools

from celery.signals import worker_process_init, worker_process_shutdown
from src.on import on_start, on_shutdown, check_connect


def sync_task(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if asyncio.get_event_loop().is_closed():
            asyncio.set_event_loop(asyncio.new_event_loop())

        async def r():
            await check_connect()
            return await f(*args, **kwargs)

        return asyncio.get_event_loop().run_until_complete(r())

    return wrapper


def create_worker():
    celery = Celery(__name__, broker=settings.BROKER_URL)
    celery.conf.update(settings.dict())
    print("Init Celery tasks app")

    return celery


task_manage = create_worker()


@worker_process_init.connect
def init_worker(**kwargs):
    if settings.ENVIRONMENT.is_deployed:
        sentry_sdk.init(
            dsn=settings.SENTRY_DSN,
            environment=settings.ENVIRONMENT,
            integrations=[CeleryIntegration()],
        )
        sentry_sdk.capture_message("run worker [name]")
    asyncio.get_event_loop().run_until_complete(on_start())


@worker_process_shutdown.connect
def shutdown_worker(**kwargs):
    asyncio.get_event_loop().run_until_complete(on_shutdown())
