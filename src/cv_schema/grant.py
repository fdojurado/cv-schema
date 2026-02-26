
from pydantic import BaseModel, ConfigDict


class Grant(BaseModel):
    name: str
    year: int
    institution_id: int

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
