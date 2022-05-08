import pytest

from src.utils.html_reader import HtmlReader


class TestHtmlReader:
    @pytest.mark.parametrize(
        "filepath, expected",
        [
            (
                "./stubs/report_excerpts/fnhc-sample.html",
                "In December 2018, the Company’s Board of Directors authorized an additional share repurchase program under which the Company may repurchase up to $10.0 million of its outstanding shares of common stock through December 31, 2019. During the year ended December 31, 2019, the Company repurchased 237,647 shares of its common stock at a total cost of $3.9 million, which is an average price per share of $16.27. The unused portion of this authorization expired on December 31, 2019.",
            ),
            (
                "./stubs/report_excerpts/earn-sample.html",
                "On June 13, 2018, our Board of Trustees approved the adoption of a share repurchase program under which we are authorized to repurchase up to 1.2 million common shares. The program, which is open-ended in duration, allows us to make repurchases from time to time on the open market or in negotiated transactions, including through Rule 10b5-1 plans. Repurchases are at our discretion, subject to applicable law, share availability, price and our financial performance, among other considerations. Under the current repurchase program adopted on June 13, 2018, we have repurchased 434,171 common shares through March 4, 2022 at an average price per share of $9.45 and an aggregate cost of $4.1 million, and have authorization to repurchase an additional 765,829 common shares. We did not purchase any shares under this program during the year ended December 31, 2021.",
            ),
            (
                "./stubs/report_excerpts/gwre-sample.html",
                "During the fiscal year ended July 31, 2021, the Company repurchased 1,488,991 shares of common stock at an average price of $109.17 per share, for an aggregate purchase price of $162.5 million. As of July 31, 2021, $37.5 million remained available for future repurchases.",
            ),
            (
                "./stubs/report_excerpts/apog-sample.html",
                "Financing Activities. Cash used by financing activities was $120.6 million in fiscal 2022, compared to $107.9 million in fiscal 2021. In fiscal 2022, we paid dividends totaling $20.3 million and repurchased 2,292,846 shares under our authorized share repurchase program, at a total cost of $100.0 million. We repurchased 1,177,704 shares under the program in fiscal 2021 and 686,997 shares under the program in fiscal 2020. We have repurchased a total of 9,425,462 shares, at a total cost of $307.3 million, since the 2004 inception of this program. We have remaining authority to repurchase 1,824,538 shares under this program, which has no expiration date, and we will continue to evaluate making future share repurchases, depending on our cash flow and debt levels, market conditions, including the continuing effects of the COVID-19 pandemic, and other potential uses of cash.",
            ),
            (
                "./stubs/report_excerpts/azz-table-sample.html",
                "Purchased under 2020 Authorization Purchased under 2012 Authorization Total Shares Repurchased Year Ended February 28, 2022 Number of shares repurchased 602 — 602 Total amount of shares repurchased $30,815 $— $30,815 Average price per share $51.20 $— $51.20 Year Ended February 28, 2021 Number of shares repurchased 331 883 1,214 Total amount of shares repurchased $15,998 $32,313 $48,311 Average price per share $48.36 $36.60 $39.80 ",
            ),
        ],
    )
    def test_read_extracts_text_from_html(self, filepath, expected):
        # assemble
        # act
        with open(filepath, "r") as f:
            html = f.read()
            text = HtmlReader.read_text(html)

        # assert
        assert text == expected
