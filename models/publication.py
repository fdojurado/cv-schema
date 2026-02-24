from dataclasses import dataclass

from models.yaml_serialize import YamlSerializable


@dataclass
class Publication(YamlSerializable):
    title: str
    journal: str
    date: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            title=yaml_data.get("title", ""),
            journal=yaml_data.get("journal", ""),
            date=yaml_data.get("date", "")
        )

    def to_yaml(self) -> dict:
        return {
            "title": self.title,
            "journal": self.journal,
            "date": self.date
        }
