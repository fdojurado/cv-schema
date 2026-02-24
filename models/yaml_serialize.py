from abc import ABC, abstractmethod


class YamlSerializable(ABC):
    @classmethod
    @abstractmethod
    def from_yaml(cls, yaml_data: dict):
        pass

    @abstractmethod
    def to_yaml(self) -> dict:
        pass
