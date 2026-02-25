from dataclasses import dataclass
from datetime import datetime, datetime0

from cv_schema.flexible_date import parse_flexible_date
from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class TeachingDate(YamlSerializable):
    start_date: datetime
    end_date: datetime

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            start_date=parse_flexible_date(yaml_data.get("start_date")),
            end_date=parse_flexible_date(yaml_data.get("end_date", ""))
        )

    def to_yaml(self) -> dict:
        return {
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat()
        }


@dataclass
class Teaching(YamlSerializable):
    id: str
    subject: str
    institution_id: int
    role: str
    url: str
    dates: list[TeachingDate]
    type: str
    responsibilities: list[str]

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            id=yaml_data.get("id", ""),
            subject=yaml_data.get("subject", ""),
            institution_id=yaml_data.get("institution_id", 0),
            role=yaml_data.get("role", ""),
            url=yaml_data.get("url", ""),
            dates=[TeachingDate.from_yaml(date)
                   for date in yaml_data.get("dates", [])],
            type=yaml_data.get("type", ""),
            responsibilities=yaml_data.get("responsibilities", [])
        )

    def to_yaml(self) -> dict:
        return {
            "id": self.id,
            "subject": self.subject,
            "institution_id": self.institution_id,
            "role": self.role,
            "url": self.url,
            "dates": [date.to_yaml() for date in self.dates],
            "type": self.type,
            "responsibilities": self.responsibilities
        }
