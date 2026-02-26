from pydantic import BaseModel, ConfigDict


class Service(BaseModel):
    id: str
    venue: str
    type: str
    evaluation_committee: str | None = None
    student_name: str | None = None
    degree_program: str | None = None
    institution_id: int | None = None
    year: int | None = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
