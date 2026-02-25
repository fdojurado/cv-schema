from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from cv_schema.yaml_serialize import YamlSerializable
from cv_schema.gs_publication import GSPublication


@dataclass
class GoogleScholarAuthor(YamlSerializable):
    name: str
    scholar_id: str
    affiliation: Optional[str] = None
    email_domain: Optional[str] = None
    interests: list[str] = field(default_factory=list)
    citedby: int = 0
    citedby5y: int = 0
    h_index: int = 0
    h_index_5y: int = 0
    i10_index: int = 0
    i10_index_5y: int = 0
    citations_per_year: dict[int, int] = field(default_factory=dict)
    publications: list[GSPublication] = field(default_factory=list)
    profile_url: Optional[str] = None
    homepage: Optional[str] = None
    data_hash: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            name=yaml_data.get("name", ""),
            scholar_id=yaml_data.get("scholar_id", ""),
            affiliation=yaml_data.get("affiliation", None),
            email_domain=yaml_data.get("email_domain", None),
            interests=yaml_data.get("interests", []),
            citedby=yaml_data.get("citedby", 0),
            citedby5y=yaml_data.get("citedby5y", 0),
            h_index=yaml_data.get("h_index", 0),
            h_index_5y=yaml_data.get("h_index_5y", 0),
            i10_index=yaml_data.get("i10_index", 0),
            i10_index_5y=yaml_data.get("i10_index_5y", 0),
            citations_per_year=yaml_data.get("citations_per_year", {}),
            publications=[GSPublication.from_yaml(
                pub) for pub in yaml_data.get("publications", [])],
            profile_url=yaml_data.get("profile_url", None),
            homepage=yaml_data.get("homepage", None),
            data_hash=yaml_data.get("data_hash", None)
        )

    def to_yaml(self) -> dict:
        return {
            "name": self.name,
            "scholar_id": self.scholar_id,
            "affiliation": self.affiliation,
            "email_domain": self.email_domain,
            "interests": self.interests,
            "citedby": self.citedby,
            "citedby5y": self.citedby5y,
            "h_index": self.h_index,
            "h_index_5y": self.h_index_5y,
            "i10_index": self.i10_index,
            "i10_index_5y": self.i10_index_5y,
            "citations_per_year": {int(year): count for year, count in self.citations_per_year.items()},
            "publications": [pub.to_yaml() for pub in self.publications],
            "profile_url": self.profile_url,
            "homepage": self.homepage,
            "data_hash": self.data_hash
        }
