from pydantic import BaseModel, Field, ConfigDict


class Research(BaseModel):
    interests: list[str] = Field(default_factory=list)
    focus: str

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
