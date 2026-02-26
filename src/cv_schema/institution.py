from pydantic import BaseModel, ConfigDict


class Institution(BaseModel):
    idx: int
    department: str
    department_short: str
    institution: str
    institution_short: str
    city: str
    country: str
    website: str

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
