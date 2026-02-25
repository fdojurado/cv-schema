from dataclasses import dataclass
from datetime import datetime

from cv_schema.flexible_date import parse_flexible_date
from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class Experience(YamlSerializable):
    institution_id: int
    position: str
    start_date: datetime
    end_date: datetime
    description: str
    responsibilities: list[str]
    achievements: list[str]

    @classmethod
    def from_yaml(cls, yaml_data: dict):

        return cls(
            institution_id=yaml_data.get("institution_id", 0),
            position=yaml_data.get("position", ""),
            start_date=parse_flexible_date(yaml_data.get("start_date")),
            end_date=parse_flexible_date(yaml_data.get("end_date", "")),
            description=yaml_data.get("description", ""),
            responsibilities=yaml_data.get("responsibilities") or [],
            achievements=yaml_data.get("achievements") or [],
        )

    def to_yaml(self) -> dict:
        return {
            "institution_id": self.institution_id,
            "position": self.position,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "description": self.description,
            "responsibilities": self.responsibilities,
            "achievements": self.achievements
        }
