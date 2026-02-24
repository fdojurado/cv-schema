
from dataclasses import dataclass
from datetime import date
from models.yaml_serialize import YamlSerializable


@dataclass
class Education(YamlSerializable):
    institution: str
    degree: str
    start_date: date
    end_date: date

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            institution=yaml_data.get("institution", ""),
            degree=yaml_data.get("degree", ""),
            start_date=date.fromisoformat(
                yaml_data.get("start_date", "1900-01-01")),
            end_date=date.fromisoformat(
                yaml_data.get("end_date", "1900-01-01"))
        )

    def to_yaml(self) -> dict:
        return {
            "institution": self.institution,
            "degree": self.degree,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
