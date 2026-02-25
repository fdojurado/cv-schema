from dataclasses import dataclass
from datetime import datetime

from cv_schema.flexible_date import parse_flexible_date
from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class Link(YamlSerializable):
    doi: str
    pdf: str
    code: str
    text: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            doi=yaml_data.get("doi", ""),
            pdf=yaml_data.get("pdf", ""),
            code=yaml_data.get("code", ""),
            text=yaml_data.get("text", "")
        )

    def to_yaml(self) -> dict:
        return {
            "doi": self.doi,
            "pdf": self.pdf,
            "code": self.code,
            "text": self.text
        }


@dataclass
class News(YamlSerializable):
    title: str
    date: datetime
    content: str
    links: list[Link]

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            title=yaml_data.get("title", ""),
            date=parse_flexible_date(yaml_data.get("date")),
            content=yaml_data.get("content", ""),
            links=[Link.from_yaml(link) for link in yaml_data.get("links", [])]
        )

    def to_yaml(self) -> dict:
        return {
            "title": self.title,
            "date": self.date.isoformat(),
            "content": self.content,
            "links": [link.to_yaml() for link in self.links]
        }
