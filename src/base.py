from datetime import datetime

from beanie import Document, before_event, Update
from pydantic import Field


class BaseDocument(Document):

    created_time: datetime = Field(default_factory=datetime.now)
    updated_time: datetime = Field(default_factory=datetime.now)

    @before_event(Update)
    def before_update(self):
        self.updated_time = datetime.now()
