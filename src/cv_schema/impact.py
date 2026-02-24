from dataclasses import dataclass
from datetime import datetime

from cv_schema.yaml_serialize import YamlSerializable


class Impact(YamlSerializable):
    citedby: int = None
    citedby5y: int = None
    h_index: int = None
    h_index5y: int = None
    i10_index: int = None
    i10_index5y: int = None
    citations_per_year: dict[str, int] = None
    updated_at: datetime = None

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            citedby=yaml_data.get("citedby", None),
            citedby5y=yaml_data.get("citedby5y", None),
            h_index=yaml_data.get("h_index", None),
            h_index5y=yaml_data.get("h_index5y", None),
            i10_index=yaml_data.get("i10_index", None),
            i10_index5y=yaml_data.get("i10_index5y", None),
            citations_per_year=yaml_data.get("citations_per_year", None),
            updated_at=datetime.fromisoformat(
                yaml_data["updated_at"]) if yaml_data.get("updated_at") else None
        )

    def to_yaml(self) -> dict:
        return {
            "citedby": self.citedby,
            "citedby5y": self.citedby5y,
            "h_index": self.h_index,
            "h_index5y": self.h_index5y,
            "i10_index": self.i10_index,
            "i10_index5y": self.i10_index5y,
            "citations_per_year": self.citations_per_year,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
