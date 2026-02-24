from dataclasses import dataclass

from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class Security(YamlSerializable):
    fingerprint: str
    public_key: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            fingerprint=yaml_data.get("fingerprint", ""),
            public_key=yaml_data.get("public_key", "")
        )

    def to_yaml(self) -> dict:
        return {
            "fingerprint": self.fingerprint,
            "public_key": self.public_key
        }
