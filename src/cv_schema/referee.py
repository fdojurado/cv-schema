from typing import Optional
from pydantic import BaseModel, ConfigDict


class Referee(BaseModel):
    id: str
    role: Optional[str] = None  # relationship to the CV author, e.g. "PhD supervisor"

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )