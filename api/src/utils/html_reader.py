import re

from bs4 import BeautifulSoup


class HtmlReader:
    @classmethod
    def read_text(cls, html: str) -> str:
        soup = BeautifulSoup(html, parser="html5lib", features="lxml")
        # using find_all(text=True) instead of get_text(strip=False)
        # to avoid incorrectly joining words together
        # for content that is in tables
        text = soup.find_all(text=True)
        text = " ".join(text)
        text = text.replace("\xa0", " ")
        text = re.sub(r"\$\s", "$", text)
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"\s\.", "", text)
        return text
