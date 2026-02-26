from pydantic import BaseModel, Field, ConfigDict


class Social(BaseModel):
    google_scholar: str = Field(default="")
    linkedin: str = Field(default="")
    github: str = Field(default="")
    orcid: str = Field(default="")
    researchgate: str = Field(default="")
    homepage: str = Field(default="")

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
