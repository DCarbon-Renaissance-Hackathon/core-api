from typing import Any, List
from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from src.constants import Environment


class Config(BaseSettings):
    ENVIRONMENT: Environment = Environment.STAGING
    DATABASE_URL: str
    # REDIS_URL: str
    SITE_DOMAIN: str = "myapp.com"

    # SENTRY_DSN: str | None

    APP_VERSION: str = "1"

    DEFAULT_AVATARS: List[str] = [
        "https://static.esollabs.com/scanhub/2023/04/12/Aprh09M1681290595s_avt1.png",
        "https://static.esollabs.com/scanhub/2023/04/12/Aprh34M1681292058s_avt2.png",
        "https://static.esollabs.com/scanhub/2023/04/12/Aprh35M1681292110s_avt3.png",
        "https://static.esollabs.com/scanhub/2023/04/12/Aprh35M1681292137s_avt4.png",
    ]
    JWT_ALG: str
    JWT_EXP: str
    JWT_SECRET: str

    class Config:
        env_file: str = ".env"
        extra: str = "allow"

    # BROKER_URL: str

    # CELERY_RESULT_BACKEND: str
    # CELERY_ENABLE_UTC = True

    # CELERY_TASK_SERIALIZER = 'json'
    # CELERY_RESULT_SERIALIZER = 'json'
    # CELERY_ACCEPT_CONTENT = ['json']

    # CELERY_ROUTES: dict = {
    #     "hello_task": {"queue": "hello"},
    #     "send_mail_task": {"queue": "mail-queue"},
    # }
    # CELERY_RESULT_DB_TABLENAMES = {
    #     'task': 'rfq_tasks',
    #     'group': 'rfq_task_group',
    # }
    # CELERY_RESULT_EXTENDED = True

    # CELERY_IMPORTS: list = ["src.tasks"]


settings = Config()

app_configs: dict[str, Any] = {"title": "App API"}
# if settings.ENVIRONMENT.is_deployed:
#     app_configs["root_path"] = f"/v{settings.APP_VERSION}"

# if not settings.ENVIRONMENT.is_debug:
#     app_configs["openapi_url"] = "/v1/asset"  # hide docs
