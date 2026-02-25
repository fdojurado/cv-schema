from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from cv_schema.yaml_serialize import YamlSerializable


class FilledStatus(Enum):
    NOT_FILLED = 1
    PARTIALLY_FILLED = 2
    FULLY_FILLED = 3


@dataclass
class GSPublication(YamlSerializable):
    """Represents a publication from Google Scholar."""

    title: str
    authors: list[str]
    type: Optional[str] = None
    year: Optional[int] = None
    citations: int = 0
    citation: Optional[str] = None
    venue: Optional[str] = None
    volume: Optional[str] = None
    number: Optional[str] = None
    pages: Optional[str] = None
    publisher: Optional[str] = None
    abstract: Optional[str] = None
    url: Optional[str] = None
    scholar_id: Optional[str] = None
    bibtex: Optional[str] = None
    citations_per_year: dict[int, int] = field(default_factory=dict)
    data_hash: Optional[str] = None
    filled: Optional[int] = FilledStatus.NOT_FILLED.value
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            title=yaml_data.get("title", ""),
            type=yaml_data.get("type", None),
            authors=yaml_data.get("authors", []),
            year=yaml_data.get("year", None),
            citations=yaml_data.get("citations", 0),
            citation=yaml_data.get("citation", None),
            venue=yaml_data.get("venue", None),
            volume=yaml_data.get("volume", None),
            number=yaml_data.get("number", None),
            pages=yaml_data.get("pages", None),
            publisher=yaml_data.get("publisher", None),
            abstract=yaml_data.get("abstract", None),
            url=yaml_data.get("url", None),
            scholar_id=yaml_data.get("scholar_id", None),
            bibtex=yaml_data.get("bibtex", None),
            citations_per_year=yaml_data.get("citations_per_year", {}),
            data_hash=yaml_data.get("data_hash", None),
            filled=FilledStatus(yaml_data.get(
                "filled", FilledStatus.NOT_FILLED.value)).value,
        )

    def to_yaml(self) -> dict:
        """Convert publication to dictionary."""
        return {
            "title": self.title,
            "type": self.type,
            "authors": self.authors,
            "year": self.year,
            "citations": self.citations,
            "citation": self.citation,
            "venue": self.venue,
            "volume": self.volume,
            "number": self.number,
            "pages": self.pages,
            "publisher": self.publisher,
            "abstract": self.abstract,
            "url": self.url,
            "scholar_id": self.scholar_id,
            "bibtex": self.bibtex,
            "citations_per_year": {int(year): count for year, count in self.citations_per_year.items()},
            "data_hash": self.data_hash,
            "filled": self.filled,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
