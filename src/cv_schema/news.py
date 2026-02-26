from datetime import date
from pydantic import BaseModel, Field, ConfigDict


class Link(BaseModel):
    text: str
    doi: str | None = None
    pdf: str | None = None
    code: str | None = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )


class News(BaseModel):
    title: str
    date: date
    content: str
    links: list[Link] = Field(default_factory=list)

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
