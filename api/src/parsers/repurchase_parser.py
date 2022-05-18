import re

from api.src.parsers.parser_protocol import ParserProtocol


class RepurchaseParser(ParserProtocol):
    pattern = r".[^.]*?repurchased.*"
    keyword = "repurchased"
    window_behind = 35
    window_ahead = 130

    def find_best_matches(self, text: str) -> [str]:
        # get indexes of all keyword matches
        match_indexes = [(x.start(), x.end()) for x in re.finditer(self.keyword, text)]

        # filter irrelevant sentences
        best_matches = []
        for x in match_indexes:
            start = x[0] - self.window_behind
            end = x[1] + self.window_ahead
            substring = text[start:end]
            best_matches.append(substring)
            match = re.search(self.pattern, substring)

            if bool(match):
                start = match.span()[0]
                end = match.span()[1]
                best_matches.append(substring[start:end])

        return list(set(best_matches))
