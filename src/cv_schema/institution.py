from dataclasses import dataclass
from datetime import datetime

from cv_schema.flexible_date import parse_flexible_date
from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class Institution(YamlSerializable):
    idx: int
    department: str
    department_short: str
    institution: str
    institution_short: str
    city: str
    country: str
    website: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            idx=yaml_data.get("idx", 0),
            department=yaml_data.get("department", ""),
            department_short=yaml_data.get("department_short", ""),
            institution=yaml_data.get("institution", ""),
            institution_short=yaml_data.get("institution_short", ""),
            city=yaml_data.get("city", ""),
            country=yaml_data.get("country", ""),
            website=yaml_data.get("website", "")
        )

    def to_yaml(self) -> dict:
        return {
            "idx": self.idx,
            "department": self.department,
            "department_short": self.department_short,
            "institution": self.institution,
            "institution_short": self.institution_short,
            "city": self.city,
            "country": self.country,
            "website": self.website
        }
