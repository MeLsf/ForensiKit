from abc import (
    ABC, 
    abstractmethod
)
from utilities import UtilitiesArtifactCollector

class ArtifactCollector(ABC):
    @abstractmethod
    def collect(self):
        ...

class ArtifactCollectorFactory:
    @staticmethod
    def create_artifact_collector(artifact_type):
        if artifact_type == "/u":
            return UtilitiesArtifactCollector()
        # elif artifact_type == "/l":
        #     return LightArtifactCollector()
        # elif artifact_type == "/m":
        #     return MemoryArtifactCollector()
        # elif artifact_type == "/s":
        #     return SensitiveArtifactCollector()
        # elif artifact_type == "/a":
        #     return AvzArtifactCollector()
        else:
            raise ValueError("Invalid artifact type")
