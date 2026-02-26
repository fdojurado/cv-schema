from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class Name(BaseModel):
    full_name: str
    preferred_name: str
    display_name: str
    citation_name: str

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )


class Personal(BaseModel):
    name: Name
    email: str
    location: str
    address: str
    phone: str

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
