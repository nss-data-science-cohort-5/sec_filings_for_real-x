from abc import ABC, abstractmethod
import spacy.tokens.span as span


class LabelerBase(ABC):
    @property
    @abstractmethod
    def labels(self) -> dict[str, str]:
        pass

    @abstractmethod
    def apply(self, text: str) -> dict[str, str]:
        pass

    @abstractmethod
    def get_date(self, obj: span) -> str:
        pass

    @abstractmethod
    def get_amount(self, obj: span) -> str:
        pass

    @abstractmethod
    def get_number(self, obj: span) -> str:
        pass
