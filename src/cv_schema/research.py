from dataclasses import dataclass

from cv_schema.yaml_serialize import YamlSerializable
from cv_schema.impact import Impact


@dataclass
class Research(YamlSerializable):
    interests: list[str]
    focus: str
    impact: Impact

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            interests=yaml_data.get("interests", []),
            focus=yaml_data.get("focus", ""),
            impact=Impact.from_yaml(yaml_data.get("impact", {}))
        )

    def to_yaml(self) -> dict:
        return {
            "interests": self.interests,
            "focus": self.focus,
            "impact": self.impact.to_yaml()
        }
