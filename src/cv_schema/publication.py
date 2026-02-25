from dataclasses import dataclass
from datetime import datetime

from cv_schema.impact import Impact

from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class PubAuthor(YamlSerializable):
    id: int
    affiliations: list[str]

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            id=yaml_data.get("id", 0),
            affiliations=yaml_data.get("affiliations", [])
        )

    def to_yaml(self) -> dict:
        return {
            "id": self.id,
            "affiliations": self.affiliations
        }


@dataclass
class Venue(YamlSerializable):
    name: str
    type: str
    abbreviation: str
    publisher: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            name=yaml_data.get("name", ""),
            type=yaml_data.get("type", ""),
            abbreviation=yaml_data.get("abbreviation", ""),
            publisher=yaml_data.get("publisher", "")
        )

    def to_yaml(self) -> dict:
        return {
            "name": self.name,
            "type": self.type,
            "abbreviation": self.abbreviation,
            "publisher": self.publisher
        }


@dataclass
class Publication(YamlSerializable):
    id: str
    title: str
    authors: list[PubAuthor]
    venue: Venue
    date: datetime
    volume: str
    issue: str
    pages: str
    doi: str
    url: str
    code: str
    slug: str
    status: str
    abstract: str
    keywords: list[str]
    copyright: str
    license: str
    bibtex: str
    impact: Impact

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            id=yaml_data.get("id", ""),
            title=yaml_data.get("title", ""),
            authors=[PubAuthor.from_yaml(
                author) for author in yaml_data.get("authors", [])],
            venue=Venue.from_yaml(yaml_data.get("venue", {})),
            date=datetime.strptime(yaml_data.get(
                "date", "1970-01-01"), "%Y-%m-%d"),
            volume=yaml_data.get("volume", ""),
            issue=yaml_data.get("issue", ""),
            pages=yaml_data.get("pages", ""),
            doi=yaml_data.get("doi", ""),
            url=yaml_data.get("url", ""),
            code=yaml_data.get("code", ""),
            slug=yaml_data.get("slug", ""),
            status=yaml_data.get("status", ""),
            abstract=yaml_data.get("abstract", ""),
            keywords=yaml_data.get("keywords", []),
            copyright=yaml_data.get("copyright", ""),
            license=yaml_data.get("license", ""),
            bibtex=yaml_data.get("bibtex", ""),
            impact=Impact.from_yaml(yaml_data.get("impact", {}))
        )

    def to_yaml(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "authors": [author.to_yaml() for author in self.authors],
            "venue": self.venue.to_yaml(),
            "date": self.date.strftime("%Y-%m-%d"),
            "volume": self.volume,
            "issue": self.issue,
            "pages": self.pages,
            "doi": self.doi,
            "url": self.url,
            "code": self.code,
            "slug": self.slug,
            "status": self.status,
            "abstract": self.abstract,
            "keywords": self.keywords,
            "copyright": self.copyright,
            "license": self.license,
            "bibtex": self.bibtex,
            "impact": self.impact.to_yaml() if self.impact else None
        }
