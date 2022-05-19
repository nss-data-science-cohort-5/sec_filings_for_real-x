from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from api.src.filing_handler import FilingHandler
from api.src.scraper.sec_scraper import SecScraper

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/report/list/<ticker>', methods=["GET"])
@cross_origin()
def reports_list(ticker: str):
	"""fetches listing of available 10K and 10Q reports"""
	scraper = SecScraper()
	reports = scraper.list_reports_for(ticker)
	return jsonify({"reports": reports})

@app.route('/report/buyback/stats', methods=["GET"])
@cross_origin()
def report_buyback_stats():
	"""fetches html document and extracts buyback stats"""
	report_url = request.args.get("report_url")
	scraper = SecScraper()
	html = scraper.get_report(report_url)
	result = FilingHandler.handle(html)
	return result


if __name__ == '__main__':
	app.run()
