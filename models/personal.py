from dataclasses import dataclass

from models.yaml_serialize import YamlSerializable


@dataclass
class PersonalInfo(YamlSerializable):
    name: str
    email: str
    phone: str
    address: str

    @classmethod
    def from_yaml(cls, yaml_data: dict):
        return cls(
            name=yaml_data.get("name", ""),
            email=yaml_data.get("email", ""),
            phone=yaml_data.get("phone", ""),
            address=yaml_data.get("address", "")
        )

    # we need to create a method to export the personal info to yaml format
    def to_yaml(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address
        }
