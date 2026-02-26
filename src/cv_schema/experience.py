from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, ConfigDict, field_validator


class Experience(BaseModel):
    institution_id: int | None = None
    position: str
    start_date: datetime
    end_date: datetime | None = None
    description: str
    responsibilities: list[str] = Field(default_factory=list)
    achievements: list[str] = Field(default_factory=list)

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )

    @field_validator("end_date", mode="before")
    @classmethod
    def parse_end_date(cls, v: Any):
        if isinstance(v, str) and v.lower() == "present":
            return None
        return v

    @property
    def is_current(self) -> bool:
        return self.end_date is None
