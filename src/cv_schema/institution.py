from pydantic import BaseModel, ConfigDict


class Institution(BaseModel):
    idx: int
    department: str | None = None
    department_short: str | None = None
    institution: str
    institution_short: str | None = None
    city: str | None = None
    country: str | None = None
    website: str | None = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
