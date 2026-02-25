from dataclasses import dataclass
from datetime import datetime
from typing import Optional

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
        def parse_date(value: Optional[str], default: str) -> datetime:
            if not value:
                return datetime.fromisoformat(default)

            # If ruamel already parsed it as datetime
            if isinstance(value, datetime):
                return value

            value_str = str(value).strip().lower()

            if value_str == "present":
                return datetime.now()

            return datetime.fromisoformat(value_str)

        return cls(
            institution_id=yaml_data.get("institution_id", 0),
            position=yaml_data.get("position", ""),
            start_date=parse_date(
                yaml_data.get("start_date"),
                "1970-01-01",
            ),
            end_date=parse_date(
                yaml_data.get("end_date"),
                datetime.now().strftime("%Y-%m-%d"),
            ),
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
