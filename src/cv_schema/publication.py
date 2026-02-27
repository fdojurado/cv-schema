from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class Visibility(Enum):
    PUBLIC = "public"
    PRIVATE = "private"


class VenueType(Enum):
    JOURNAL = "journal"
    CONFERENCE = "conference"
    WORK_IN_PROGRESS = "work-in-progress"


class PubAuthor(BaseModel):
    id: str
    affiliations: list[int] = Field(default_factory=list)


class Venue(BaseModel):
    name: str | None = None
    type: VenueType = VenueType.JOURNAL
    abbreviation: str | None = None
    publisher: str | None = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )


class Impact(BaseModel):
    citedby: int
    citations_per_year: dict[int, int] = Field(default_factory=dict)

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )


class Publication(BaseModel):
    id: str
    title: str

    authors: list[PubAuthor] = Field(default_factory=list)
    venue: Venue | None = None
    date: datetime

    volume: int | None = None
    issue: int | None = None
    pages: str | None = None

    doi: str | None = None
    url: HttpUrl | None = None
    code: str | None = None

    slug: str | None = None
    status: str | None = None
    abstract: str | None = None
    keywords: list[str] = Field(default_factory=list)

    copyright: str | None = None
    license: str | None = None
    bibtex: str | None = None

    impact: Impact | None = None

    visibility: Visibility = Visibility.PUBLIC

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
