import re

import spacy

from src.labelers.labeler_protocol import LabelerProtocol


class RepurchaseLabeler(LabelerProtocol):
    def get_named_entities(self, texts) -> [dict[str, str]]:
        labels = []
        nlp = spacy.load("en_core_web_md")

        for text in texts:
            doc = nlp(text)
            x = {}
            for ent in doc.ents:
                if ent.label_ == "DATE" and not x.get("date"):
                    x["date"] = self.get_date(ent)
                elif ent.label_ == "CARDINAL" and not x.get("number"):
                    x["number"] = self.get_number(ent)
                elif ent.label_ == "MONEY" and not x.get("amount"):
                    x["amount"] = self.get_amount(ent)

                if not all(x.values()):
                    continue

                if not len(x.keys()) == 3:
                    continue

                labels.append(x)

        # remove any duplicates
        labels_cleaned = []
        [labels_cleaned.append(dict(t)) for t in {tuple(sorted(d.items())) for d in labels}]
        return labels_cleaned

    def get_date(self, obj) -> str:
        # must have at least a four digit year
        if obj.text and re.search(r'\d{4}', obj.text):
            return obj.text

    def get_number(self, obj) -> str:
        # must have at least one digit
        if obj.text and bool(re.search(r'\d*,\d*', obj.text)):
            return obj.text

    def get_amount(self, obj) -> str:
        if bool(re.search(r'\d*', obj.text)) and bool(re.search(r"(\$|thousand|million|billion)", obj.text)):
            return obj.text
