from typing import Union

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from api.src.scraper.models.report_item import ReportItem
from selenium import webdriver
import pandas as pd
import json


class SecScraper:
	diver: WebDriver

	def __init__(self):
		self.driver = webdriver.Firefox()

	def list_reports_for(self, ticker: str) -> [ReportItem]:
		"""scrapes sec.gov website for links to all available company 10-K and 10-Q reports"""
		# visit https://www.sec.gov/edgar/searchedgar/companysearch.html
		self.driver.get("https://www.sec.gov/edgar/searchedgar/companysearch.html")

		# enter ticker in search box
		el = self.driver.find_element(by=By.ID, value="company")

		# select top matching result from popup window to visit search results page
		el.send_keys(ticker)
		self.driver.implicitly_wait(30)
		els = self.driver.find_elements(by=By.CLASS_NAME, value="smart-search-hint-entity")
		if not any(els):
			return []
		els[0].click()
		self.driver.implicitly_wait(30)

		# on search results page, open 10-k dropdown then clicks "View all 10-ks and 10-qs"
		el = self.driver.find_element(by=By.XPATH, value="//h5[contains(text(), '10-K')]")
		self.driver.implicitly_wait(30)
		el.click()
		self.driver.implicitly_wait(30)
		el = self.driver.find_element(by=By.CSS_SELECTOR, value="button[data-group=annualOrQuarterlyReports]")

		# ensure button element is in view before click attempt
		self.driver.execute_script(f"javascript:window.scrollBy({el.location['x']}, {el.location['y']})")
		self.driver.implicitly_wait(30)
		el.click()
		self.driver.implicitly_wait(30)

		# find the html for the 10k 10q report results table
		el = self.driver.find_element(by=By.ID, value="filingsTable")
		html_table = el.get_attribute("outerHTML")
		link_els = self.driver.find_element(by=By.ID, value="filingsTable").find_elements(by=By.CLASS_NAME, value="document-link")
		links = [link.get_attribute("href") for link in link_els]

		# build a dataframe from the html table content
		df = pd.read_html(html_table, flavor="html5lib")[0]
		df["form_link"] = links
		df["Form description"] = df["Form description"].apply(lambda x: x.split("Open document")[0])
		df["Reporting date"] = df["Reporting date"].apply(lambda x: x.split("View all")[0])
		df.columns = [x.lower().replace(" ", "_") for x in df.columns]

		# convert the dataframe to json and close the driver
		result = df.to_json(orient="records")
		parsed = json.loads(result)
		self.driver.quit()
		return parsed

	def get_report(self, report_url: str) -> str:
		self.driver.get(report_url)
		self.driver.implicitly_wait(30)
		report = self.driver.page_source
		self.driver.quit()
		return report





