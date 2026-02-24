from dataclasses import dataclass
from datetime import date
from cv_schema.education import Education
from cv_schema.experience import Experience
from cv_schema.personal import PersonalInfo
from cv_schema.research import Research
from cv_schema.publication import Publication
from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class CVModel(YamlSerializable):
    personal: PersonalInfo
    education: list[Education]
    experience: list[Experience]
    research: list[Research]
    publications: list[Publication]

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            personal=PersonalInfo.from_yaml(yaml_data.get("personal", {})),
            education=[Education.from_yaml(ed)
                       for ed in yaml_data.get("education", [])],
            experience=[Experience.from_yaml(
                exp) for exp in yaml_data.get("experience", [])],
            research=[Research.from_yaml(res)
                      for res in yaml_data.get("research", [])],
            publications=[Publication.from_yaml(
                pub) for pub in yaml_data.get("publications", [])]
        )

    def to_yaml(self) -> dict:
        return {
            "personal": self.personal.to_yaml(),
            "education": [ed.to_yaml() for ed in self.education],
            "experience": [exp.to_yaml() for exp in self.experience],
            "research": [res.to_yaml() for res in self.research],
            "publications": [pub.to_yaml() for pub in self.publications]
        }
