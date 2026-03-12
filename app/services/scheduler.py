from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import Awaitable, Callable

from app.core.config import settings


def create_scheduler(job: Callable[[], Awaitable[None]]) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        job,
        trigger="interval",
        seconds=settings.parse_schedule_minutes * 60,
        coalesce=True,
        max_instances=1,
    )
    return scheduler
