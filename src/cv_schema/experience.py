from dataclasses import dataclass
from datetime import datetime

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
            start_date=datetime.strptime(
                yaml_data.get("start_date", "1970-01"), "%Y-%m"),
            end_date=datetime.strptime(
                yaml_data.get("end_date", "1970-01"), "%Y-%m"),
            description=yaml_data.get("description", ""),
            responsibilities=yaml_data.get("responsibilities", []),
            achievements=yaml_data.get("achievements", [])
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
