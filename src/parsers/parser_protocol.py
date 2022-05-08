from typing import Protocol


class ParserProtocol(Protocol):
    """regex pattern"""

    pattern: str

    """keyword used in search"""
    keyword: str

    """window behind index of keyword match"""
    window_behind: int

    """window ahead index of keyword match"""
    window_ahead: int

    def find_best_matches(self, text: str) -> [str]:
        """uses the indexes of all matches to return the best matching sentences from the text"""
