from dataclasses import dataclass

from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class Grant(YamlSerializable):
    name: str
    year: int
    institution_id: int

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            name=yaml_data.get("name", ""),
            year=yaml_data.get("year", 0),
            institution_id=yaml_data.get("institution_id", 0)
        )

    def to_yaml(self) -> dict:
        return {
            "name": self.name,
            "year": self.year,
            "institution_id": self.institution_id
        }
