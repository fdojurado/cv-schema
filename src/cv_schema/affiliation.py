from pydantic import BaseModel, ConfigDict


class Affiliation(BaseModel):
    institution_id: int
    current: bool

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
