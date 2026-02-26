from cv_schema.affiliation import Affiliation
from cv_schema.personal import Personal
from cv_schema.social import Social

from pydantic import BaseModel, Field, ConfigDict


class CoAuthor(BaseModel):
    id: str
    personal: Personal
    title: str | None = None
    affiliations: list[Affiliation] = Field(default_factory=list)
    social: Social | None = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
