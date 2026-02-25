from dataclasses import dataclass

from cv_schema.yaml_serialize import YamlSerializable

@dataclass
class TeachingDate(YamlSerializable):
    start_date: str
    end_date: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            start_date=yaml_data.get("start_date", ""),
            end_date=yaml_data.get("end_date", "")
        )

    def to_yaml(self) -> dict:
        return {
            "start_date": self.start_date,
            "end_date": self.end_date
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
    
