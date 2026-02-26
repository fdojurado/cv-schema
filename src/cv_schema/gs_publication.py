from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class FilledStatus(Enum):
    NOT_FILLED = 1
    PARTIALLY_FILLED = 2
    FULLY_FILLED = 3


class GSPublication(BaseModel):
    """Represents a publication from Google Scholar."""

    title: str
    authors: list[str]
    type: Optional[str] = None
    year: Optional[int] = None
    citations: int = 0
    citation: Optional[str] = None
    venue: Optional[str] = None
    volume: Optional[str] = None
    number: Optional[str] = None
    pages: Optional[str] = None
    publisher: Optional[str] = None
    abstract: Optional[str] = None
    url: Optional[str] = None
    scholar_id: Optional[str] = None
    bibtex: Optional[str] = None
    citations_per_year: dict[int, int] = Field(default_factory=dict)
    data_hash: Optional[str] = None
    filled: Optional[int] = Field(
        default_factory=lambda: FilledStatus.NOT_FILLED.value)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
