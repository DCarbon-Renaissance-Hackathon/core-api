import os
from src.constants import Environment
from src.config import settings

os.environ["TZ"] = "UTC"

from src.on import on_start
from fastapi import FastAPI
from src.config import app_configs, settings
from src.user.router import router as user_router
from src.certificate.router import router as certificate_router
from src.auth.router import router as auth_router

app = FastAPI(
    **app_configs,
    openapi_prefix="/api/core" if settings.ENVIRONMENT == Environment.STAGING else "",
)

print(settings.ENVIRONMENT)


@app.on_event("startup")
async def lifespan():
    # Startup
    await on_start()


# @app.on_event("shutdown")
# async def shutdown():
#     # Shutdown
#     # await on_shutdown()


# if settings.ENVIRONMENT.is_deployed:
#     sentry_sdk.init(
#         dsn=settings.SENTRY_DSN,
#         environment=settings.ENVIRONMENT,
#         integrations=[FastApiIntegration()],
#     )
#     sentry_sdk.capture_message("Start [name] api")


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


certificate_router
app.include_router(user_router, prefix="/user", tags=["Users"])
app.include_router(certificate_router, prefix="/certificate", tags=["Certificate"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
