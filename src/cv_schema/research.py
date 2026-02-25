from dataclasses import dataclass

from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class Research(YamlSerializable):
    interests: list[str]
    focus: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            interests=yaml_data.get("interests", []),
            focus=yaml_data.get("focus", "")
        )

    def to_yaml(self) -> dict:
        return {
            "interests": self.interests,
            "focus": self.focus
        }
