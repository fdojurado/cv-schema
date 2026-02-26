from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class Security(BaseModel):
    fingerprint: str
    public_key: str

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )
