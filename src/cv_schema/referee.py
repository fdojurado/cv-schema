from pydantic import BaseModel, ConfigDict


class Referee(BaseModel):
    id: str

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
