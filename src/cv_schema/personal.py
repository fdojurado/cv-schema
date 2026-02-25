from dataclasses import dataclass

from cv_schema.yaml_serialize import YamlSerializable


@dataclass
class AuthorName(YamlSerializable):
    full_name: str
    preferred_name: str
    display_name: str
    citation_name: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            full_name=yaml_data.get("full_name", ""),
            preferred_name=yaml_data.get("preferred_name", ""),
            display_name=yaml_data.get("display_name", ""),
            citation_name=yaml_data.get("citation_name", "")
        )

    def to_yaml(self) -> dict:
        return {
            "full_name": self.full_name,
            "preferred_name": self.preferred_name,
            "display_name": self.display_name,
            "citation_name": self.citation_name
        }


@dataclass
class PersonalInfo(YamlSerializable):
    name: AuthorName
    email: str
    location: str
    address: str
    phone: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            name=AuthorName.from_yaml(yaml_data.get("name", {})),
            email=yaml_data.get("email", ""),
            location=yaml_data.get("location", ""),
            address=yaml_data.get("address", ""),
            phone=yaml_data.get("phone", "")
        )

    def to_yaml(self) -> dict:
        return {
            "name": self.name.to_yaml(),
            "email": self.email,
            "location": self.location,
            "address": self.address,
            "phone": self.phone
        }
