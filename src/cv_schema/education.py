
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class Education(BaseModel):
    degree: str
    institution_id: int
    start_date: datetime
    end_date: datetime
    thesis_title: str
    thesis_url: str
    advisor_keys: list[str] = Field(default_factory=list)
    awards: list[str] = Field(default_factory=list)

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
