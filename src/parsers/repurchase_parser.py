import re

from src.parsers.parser_base import ParserBase


class RepurchaseParser(ParserBase):
    def pattern(self):
        return r"During.*repurchased.*(?=shares).+(?=cost|price).*(?=\;\s\w?|\.\s\w)"

    def read(self, text: str):
        match = re.search(self.pattern(), text)
        if bool(match):
            start = match.span()[0]
            end = match.span()[1]
            return text[start:end]
        else:
            return "N/A"
