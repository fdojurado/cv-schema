from dataclasses import dataclass
from datetime import datetime

from cv_schema.yaml_serialize import YamlSerializable

from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class PubAuthor(BaseModel, YamlSerializable):
    id: str
    affiliations: list[int] = Field(default_factory=list)


class Venue(BaseModel, YamlSerializable):
    name: str
    type: str
    abbreviation: str
    publisher: str


class Impact(BaseModel, YamlSerializable):
    citedby: int
    citations_per_year: dict[int, int] = Field(default_factory=dict)


class Publication(BaseModel, YamlSerializable):
    id: str
    title: str

    authors: list[PubAuthor] = Field(default_factory=list)
    venue: Venue
    date: datetime

    volume: int | None = None
    issue: int | None = None
    pages: str | None = None

    doi: str | None = None
    url: HttpUrl | None = None
    code: str | None = None

    slug: str
    status: str
    abstract: str | None = None
    keywords: list[str] = Field(default_factory=list)

    copyright: str | None = None
    license: str | None = None
    bibtex: str | None = None

    impact: Impact | None = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
