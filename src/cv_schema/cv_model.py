from dataclasses import dataclass
from datetime import date
from cv_schema.education import Education
from cv_schema.experience import Experience
from cv_schema.personal import PersonalInfo
from cv_schema.google_scholar_author import GoogleScholarAuthor
from cv_schema.publication import Publication
from cv_schema.social import Social
from cv_schema.research import Research
from cv_schema.grant import Grant
from cv_schema.affiliation import Affiliation
from cv_schema.security import Security
from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class CVModel(YamlSerializable):
    personal: PersonalInfo
    social: Social
    education: list[Education]
    research: Research
    experience: list[Experience]
    google_scholar_author: GoogleScholarAuthor
    publications: list[Publication]
    grants: list[Grant]
    affiliations: list[Affiliation]
    long_intro: str
    short_intro: str
    security: Security

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            personal=PersonalInfo.from_yaml(yaml_data.get("personal", {})),
            social=Social.from_yaml(yaml_data.get("social", {})),
            education=[Education.from_yaml(edu)
                       for edu in yaml_data.get("education", [])],
            research=Research.from_yaml(yaml_data.get("research", {})),
            experience=[Experience.from_yaml(
                exp) for exp in yaml_data.get("experience", [])],
            google_scholar_author=GoogleScholarAuthor.from_yaml(
                yaml_data.get("google_scholar_author", {})),
            publications=[Publication.from_yaml(
                pub) for pub in yaml_data.get("publications", [])],
            grants=[Grant.from_yaml(grant)
                    for grant in yaml_data.get("grants", [])],
            affiliations=[Affiliation.from_yaml(
                aff) for aff in yaml_data.get("affiliations", [])],
            long_intro=yaml_data.get("long_intro", ""),
            short_intro=yaml_data.get("short_intro", ""),
            security=Security.from_yaml(yaml_data.get("security", {}))
        )

    def to_yaml(self) -> dict:
        return {
            "personal": self.personal.to_yaml(),
            "social": self.social.to_yaml(),
            "education": [edu.to_yaml() for edu in self.education],
            "research": self.research.to_yaml(),
            "experience": [exp.to_yaml() for exp in self.experience],
            "google_scholar_author": self.google_scholar_author.to_yaml(),
            "publications": [pub.to_yaml() for pub in self.publications],
            "grants": [grant.to_yaml() for grant in self.grants],
            "affiliations": [aff.to_yaml() for aff in self.affiliations],
            "long_intro": self.long_intro,
            "short_intro": self.short_intro,
            "security": self.security.to_yaml()
        }
