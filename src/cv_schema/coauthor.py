from cv_schema.affiliation import Affiliation
from cv_schema.personal import Personal
from cv_schema.social import Social

from pydantic import BaseModel, Field, ConfigDict


class CoAuthor(BaseModel):
    id: int
    personal: Personal
    title: str
    affiliations: list[Affiliation] = Field(default_factory=list)
    social: Social

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
