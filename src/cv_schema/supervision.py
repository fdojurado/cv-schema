from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class Supervision(BaseModel):
    students: list[str] = Field(default_factory=list)
    year: int
    degree: str
    degree_short: str
    institution_id: int
    type: str
    supervisor_ids: list[int] = Field(default_factory=list)
    thesis_title: str | None = None
    thesis_url: HttpUrl | None = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
