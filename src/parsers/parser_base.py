from abc import ABC, abstractmethod


class ParserBase(ABC):
    @abstractmethod
    def pattern(self) -> str:
        pass

    @abstractmethod
    def read(self, text: str) -> str:
        pass
