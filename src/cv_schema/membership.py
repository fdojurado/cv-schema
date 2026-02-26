from pydantic import BaseModel, ConfigDict

class Membership(BaseModel):
    id: str
    name: str
    type: str
    year: int | None = None
    
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )