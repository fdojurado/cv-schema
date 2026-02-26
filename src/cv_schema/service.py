from pydantic import BaseModel, ConfigDict


class Service(BaseModel):
    id: str
    type: str
    venue: str | None = None
    evaluation_committee: str | None = None
    student_name: str | None = None
    degree_program: str | None = None
    institution_id: int | None = None
    year: int | None = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
