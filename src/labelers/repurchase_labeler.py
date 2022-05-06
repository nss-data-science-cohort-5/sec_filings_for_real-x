import re

import spacy

from src.labelers.labeler_base import LabelerBase


class RepurchaseLabeler(LabelerBase):
	labels = {}

	def apply(self, text) -> dict[str, str]:
		nlp = spacy.load("en_core_web_md")
		doc = nlp(text)
		for ent in doc.ents:
			if ent.label_ == "DATE":
				self.labels["date"] = self.get_date(ent)
			elif ent.label_ == "CARDINAL":
				self.labels["number"] = self.get_number(ent)
			elif ent.label_ == "MONEY":
				self.labels["amount"] = self.get_amount(ent)
		return self.labels

	def get_date(self, obj) -> str:
		return obj.text

	def get_number(self, obj) -> str:
		return obj.text

	def get_amount(self, obj) -> str:
		if bool(re.search(r'(\$|million|billion)', obj.text)):
			return obj.text
		else:
			return ""

