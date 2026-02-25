from dataclasses import dataclass

from cv_schema.education import Education
from cv_schema.experience import Experience
from cv_schema.teaching import Teaching
from cv_schema.personal import Personal
from cv_schema.google_scholar_author import GoogleScholarAuthor
from cv_schema.gs_publication import GSPublication
from cv_schema.publication import Publication
from cv_schema.affiliation import Affiliation
from cv_schema.coauthor import CoAuthor
from cv_schema.research import Research
from cv_schema.security import Security
from cv_schema.social import Social
from cv_schema.grant import Grant

from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class CVModel(YamlSerializable):
    title: str
    personal: Personal
    social: Social
    education: list[Education]
    research: Research
    experiences: list[Experience]
    teaching: list[Teaching]
    google_scholar_author: GoogleScholarAuthor
    publications: list[Publication]
    coauthors: list[CoAuthor]
    grants: list[Grant]
    affiliations: list[Affiliation]
    long_intro: str
    short_intro: str
    security: Security

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            title=yaml_data.get("title", ""),
            personal=Personal.from_yaml(yaml_data.get("personal", {})),
            social=Social.from_yaml(yaml_data.get("social", {})),
            education=[Education.from_yaml(edu)
                       for edu in yaml_data.get("education", [])],
            research=Research.from_yaml(yaml_data.get("research", {})),
            experiences=[Experience.from_yaml(
                exp) for exp in yaml_data.get("experiences", [])],
            teaching=[Teaching.from_yaml(
                teach) for teach in yaml_data.get("teaching", [])],
            google_scholar_author=GoogleScholarAuthor.from_yaml(
                yaml_data.get("google_scholar_author", {})),
            publications=[GSPublication.from_yaml(
                pub) for pub in yaml_data.get("publications", [])],
            coauthors=[CoAuthor.from_yaml(coauth)
                       for coauth in yaml_data.get("coauthors", [])],
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
            "title": self.title,
            "personal": self.personal.to_yaml(),
            "social": self.social.to_yaml(),
            "education": [edu.to_yaml() for edu in self.education],
            "research": self.research.to_yaml(),
            "experiences": [exp.to_yaml() for exp in self.experiences],
            "teaching": [teach.to_yaml() for teach in self.teaching],
            "google_scholar_author": self.google_scholar_author.to_yaml(),
            "publications": [pub.to_yaml() for pub in self.publications],
            "coauthors": [coauth.to_yaml() for coauth in self.coauthors],
            "grants": [grant.to_yaml() for grant in self.grants],
            "affiliations": [aff.to_yaml() for aff in self.affiliations],
            "long_intro": self.long_intro,
            "short_intro": self.short_intro,
            "security": self.security.to_yaml()
        }
