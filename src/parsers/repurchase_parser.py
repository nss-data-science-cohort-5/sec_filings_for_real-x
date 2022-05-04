import re

from src.parsers.parser_base import ParserBase


class RepurchaseParser(ParserBase):
    def pattern(self):
        return r"(?<=\.\s)?During.*repurchased.*(?=shares).+(?=cost|price).*(?=\;\s\w?|\.\s\w)"

    def read(self, text: str):
        match = re.match(self.pattern(), text)
        if bool(match):
            start = match.span()
            end = match.span()
            return text[start:end]
        else:
            return "N/A"
