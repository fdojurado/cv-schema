from dataclasses import dataclass

from cv_schema.yaml_serialize import YamlSerializable


class Social(YamlSerializable):
    google_scholar: str
    linkedin: str
    github: str
    orcid: str
    researchgate: str
    homepage: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            google_scholar=yaml_data.get("google_scholar", ""),
            linkedin=yaml_data.get("linkedin", ""),
            github=yaml_data.get("github", ""),
            orcid=yaml_data.get("orcid", ""),
            researchgate=yaml_data.get("researchgate", ""),
            homepage=yaml_data.get("homepage", "")
        )

    def to_yaml(self) -> dict:
        return {
            "google_scholar": self.google_scholar,
            "linkedin": self.linkedin,
            "github": self.github,
            "orcid": self.orcid,
            "researchgate": self.researchgate,
            "homepage": self.homepage
        }
