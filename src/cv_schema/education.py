
from dataclasses import dataclass
from datetime import datetime
from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class Education(YamlSerializable):
    degree: str
    institution_id: int
    start_date: datetime
    end_date: datetime
    thesis_title: str
    thesis_url: str
    advisor_keys: list[str]
    awards: list[str]

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            degree=yaml_data.get("degree", ""),
            institution_id=yaml_data.get("institution_id", 0),
            start_date=datetime.fromisoformat(
                yaml_data.get("start_date", "1900-01-01")),
            end_date=datetime.fromisoformat(
                yaml_data.get("end_date", "1900-01-01")),
            thesis_title=yaml_data.get("thesis_title", ""),
            thesis_url=yaml_data.get("thesis_url", ""),
            advisor_keys=yaml_data.get("advisor_keys", []),
            awards=yaml_data.get("awards", [])
        )

    def to_yaml(self) -> dict:
        return {
            "degree": self.degree,
            "institution_id": self.institution_id,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "thesis_title": self.thesis_title,
            "thesis_url": self.thesis_url,
            "advisor_keys": self.advisor_keys,
            "awards": self.awards
        }
