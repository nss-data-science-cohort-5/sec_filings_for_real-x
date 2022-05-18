from typing import Protocol

import spacy.tokens.span as span


class LabelerProtocol(Protocol):
    def get_named_entities(self, texts: [str]) -> [dict[str, str]]:
        """returns dictionary of named entities from text"""

    def get_date(self, obj: span) -> str:
        """returns the DATE named entity"""

    def get_amount(self, obj: span) -> str:
        """returns the MONEY named entity"""

    def get_number(self, obj: span) -> str:
        """returns the CARDINAL named entity"""
