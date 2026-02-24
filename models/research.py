from dataclasses import dataclass

from models.yaml_serialize import YamlSerializable


@dataclass
class Research(YamlSerializable):
    title: str
    description: str
    date: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            title=yaml_data.get("title", ""),
            description=yaml_data.get("description", ""),
            date=yaml_data.get("date", "")
        )

    def to_yaml(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "date": self.date
        }
