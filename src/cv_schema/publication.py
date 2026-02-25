from dataclasses import dataclass

from cv_schema.yaml_serialize import YamlSerializable

@dataclass
class PubAuthor(YamlSerializable):
    id: int
    affiliations: list[str]

@dataclass
class Publication(YamlSerializable):
    id: str
    title: str
    authors: list[PubAuthor]