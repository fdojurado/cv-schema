from datetime import datetime
from typing import Optional
from enum import Enum, auto


from cv_schema.gs_publication import GSPublication

from pydantic import BaseModel, Field, ConfigDict


class Status(Enum):
    NOT_FILLED = auto()
    PARTIALLY_FILLED = auto()
    FULLY_FILLED = auto()


class GoogleScholarAuthor(BaseModel):
    name: str
    scholar_id: str
    affiliation: Optional[str] = None
    email_domain: Optional[str] = None
    interests: list[str] = Field(default_factory=list)
    citedby: int = 0
    citedby5y: int = 0
    h_index: int = 0
    h_index_5y: int = 0
    i10_index: int = 0
    i10_index_5y: int = 0
    citations_per_year: dict[int, int] = Field(default_factory=dict)
    publications: list[GSPublication] = Field(default_factory=list)
    profile_url: Optional[str] = None
    homepage: Optional[str] = None
    status: Status = Status.NOT_FILLED
    data_hash: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
