from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class Name(BaseModel):
    full_name: str | None = None
    preferred_name: str | None = None
    display_name: str | None = None
    citation_name: str | None = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )


class Personal(BaseModel):
    name: Name
    email: str | None = None
    location: str | None = None
    address: str | None = None
    phone: str | None = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
