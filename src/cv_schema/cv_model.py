from dataclasses import dataclass
from datetime import date
from cv_schema.education import Education
from cv_schema.experience import Experience
from cv_schema.personal import PersonalInfo
from src.cv_schema.google_scholar_author import GoogleScholarAuthor
from cv_schema.publication import Publication
from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class CVModel(YamlSerializable):
    personal: PersonalInfo
    education: list[Education]
    experience: list[Experience]
    google_scholar_author: GoogleScholarAuthor
    publications: list[Publication]

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            personal=PersonalInfo.from_yaml(yaml_data.get("personal", {})),
            education=[Education.from_yaml(ed)
                       for ed in yaml_data.get("education", [])],
            experience=[Experience.from_yaml(
                exp) for exp in yaml_data.get("experience", [])],
            google_scholar_author=GoogleScholarAuthor.from_yaml(
                yaml_data.get("google_scholar_author", {})),
            publications=[Publication.from_yaml(
                pub) for pub in yaml_data.get("publications", [])]
        )

    def to_yaml(self) -> dict:
        return {
            "personal": self.personal.to_yaml(),
            "education": [ed.to_yaml() for ed in self.education],
            "experience": [exp.to_yaml() for exp in self.experience],
            "google_scholar_author": self.google_scholar_author.to_yaml(),
            "publications": [pub.to_yaml() for pub in self.publications]
        }
