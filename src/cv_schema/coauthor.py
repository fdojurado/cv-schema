from dataclasses import dataclass

from cv_schema.affiliation import Affiliation
from cv_schema.personal import Personal
from cv_schema.social import Social
from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class CoAuthor(YamlSerializable):
    id: int
    personal: Personal
    title: str
    affiliations: list[Affiliation]
    social: Social

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            id=yaml_data.get("id", 0),
            personal=Personal.from_yaml(yaml_data.get("personal", {})),
            title=yaml_data.get("title", ""),
            affiliations=[Affiliation.from_yaml(
                aff) for aff in yaml_data.get("affiliations", [])],
            social=Social.from_yaml(yaml_data.get("social", {}))
        )

    def to_yaml(self) -> dict:
        return {
            "id": self.id,
            "personal": self.personal.to_yaml(),
            "title": self.title,
            "affiliations": [aff.to_yaml() for aff in self.affiliations],
            "social": self.social.to_yaml()
        }
