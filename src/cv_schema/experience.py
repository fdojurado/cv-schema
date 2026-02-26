from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class Experience(BaseModel):
    institution_id: int | None = None
    position: str
    start_date: datetime
    end_date: datetime
    description: str
    responsibilities: list[str] = Field(default_factory=list)
    achievements: list[str] = Field(default_factory=list)

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
