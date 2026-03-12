from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional


class ExternalCity(BaseModel):
    id: int
    name: str


class ExternalTag(BaseModel):
    id: int
    name: str
    description: str


class ExternalTimetableMode(BaseModel):
    id: int
    name: str


class ExternalVacancyItem(BaseModel):
    id: int
    title: str
    timetable_mode: ExternalTimetableMode
    tag: ExternalTag
    city: Optional[ExternalCity]
    published_at: datetime
    is_remote_available: bool
    is_hot: bool


class ExternalVacanciesResponse(BaseModel):
    item_count: int = Field(alias="item_count")
    items: List[ExternalVacancyItem]
    items_per_page: int
    page: int
    page_count: int
