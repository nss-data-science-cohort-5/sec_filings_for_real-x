from typing import Protocol


class PipelineProtocol(Protocol):
    def run(self, html: str) -> dict[str, str]:
        """returns dictionary containing date, amount, and number"""
