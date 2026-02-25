from dataclasses import dataclass

from cv_schema.yaml_serialize import YamlSerializable

@dataclass
class Affiliation(YamlSerializable):
    institution_id: int
    current: bool
    
    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            institution_id=yaml_data.get("institution_id", 0),
            current=yaml_data.get("current", False)
        )
        
    def to_yaml(self) -> dict:
        return {
            "institution_id": self.institution_id,
            "current": self.current
        }