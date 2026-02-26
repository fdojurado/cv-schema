from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class TeachingDate(BaseModel):
    start_date: datetime
    end_date: datetime

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )


class Teaching(BaseModel):
    id: str
    subject: str
    institution_id: int
    role: str
    url: str
    dates: list[TeachingDate] = Field(default_factory=list)
    type: str
    responsibilities: list[str] = Field(default_factory=list)

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
