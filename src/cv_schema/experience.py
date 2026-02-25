from dataclasses import dataclass

from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class Experience(YamlSerializable):
    institution_id: int
    position: str
    start_date: str
    end_date: str
    description: str
    responsibilities: list[str]
    achievements: list[str]

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            company=yaml_data.get("company", ""),
            position=yaml_data.get("position", ""),
            start_date=yaml_data.get("start_date", ""),
            end_date=yaml_data.get("end_date", "")
        )

    def to_yaml(self) -> dict:
        return {
            "company": self.company,
            "position": self.position,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
