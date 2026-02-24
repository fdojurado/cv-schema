
from dataclasses import dataclass
from datetime import datetime
from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class Education(YamlSerializable):
    degree: str
    institution_id: int
    year_start: datetime
    year_end: datetime
    thesis_title: str
    thesis_url: str
    advisor_keys: list[str]
    awards: list[str]

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            degree=yaml_data.get("degree", ""),
            institution_id=yaml_data.get("institution_id", 0),
            year_start=datetime.fromisoformat(
                yaml_data.get("year_start", "1900-01-01")),
            year_end=datetime.fromisoformat(
                yaml_data.get("year_end", "1900-01-01")),
            thesis_title=yaml_data.get("thesis_title", ""),
            thesis_url=yaml_data.get("thesis_url", ""),
            advisor_keys=yaml_data.get("advisor_keys", []),
            awards=yaml_data.get("awards", [])
        )

    def to_yaml(self) -> dict:
        return {
            "degree": self.degree,
            "institution_id": self.institution_id,
            "year_start": self.year_start.isoformat(),
            "year_end": self.year_end.isoformat(),
            "thesis_title": self.thesis_title,
            "thesis_url": self.thesis_url,
            "advisor_keys": self.advisor_keys,
            "awards": self.awards
        }
