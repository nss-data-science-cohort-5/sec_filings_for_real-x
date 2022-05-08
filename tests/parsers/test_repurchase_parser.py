import pytest

from src.parsers.repurchase_parser import RepurchaseParser


class TestRepurchaseParser:
    def test_read_returns_na(self):
        # assemble
        text = "no matches here"
        parser = RepurchaseParser()

        # act
        result = parser.find_best_matches(text)

        # assert
        assert result == "N/A"

    @pytest.mark.parametrize(
        "text, expected",
        [
            (
                "Repurchases are at the Company's discretion, subject to applicable law, share availability, price and its financial performance, among other considerations. During the year ended December 31, 2020, the Company repurchased 136,142 of its common shares at an aggregate cost of $1.0 million, and an average price per share of $7.24; the Company did not repurchase any shares during the year ended December 31, 2021. From inception of the current share repurchase program adopted on June 13, 2018 through December 31, 2021, the Company repurchased 434,171 of its common shares at an aggregate cost of $4.1 million, and an average price per share of $9.45.",
                "During the year ended December 31, 2020, the Company repurchased 136,142 of its common shares at an aggregate cost of $1.0 million, and an average price per share of $7.24; the Company did not repurchase any shares during the year ended December 31, 2021",
            ),
            (
                "In December 2018, the Company’s Board of Directors authorized an additional share repurchase program under which the Company may repurchase up to $10.0 million of its outstanding shares of common stock through December 31, 2019. During the year ended December 31, 2019, the Company repurchased 237,647 shares of its common stock at a total cost of $3.9 million, which is an average price per share of $16.27. The unused portion of this authorization expired on December 31, 2019.",
                "During the year ended December 31, 2019, the Company repurchased 237,647 shares of its common stock at a total cost of $3.9 million, which is an average price per share of $16.27",
            ),
            (
                "During the fiscal year ended July 31, 2021, the Company repurchased 1,488,991 shares of common stock at an average price of $109.17 per share, for an aggregate purchase price of $162.5 million. As of July 31, 2021, $37.5 million remained available for future repurchases.",
                "During the fiscal year ended July 31, 2021, the Company repurchased 1,488,991 shares of common stock at an average price of $109.17 per share, for an aggregate purchase price of $162.5 million",
            ),
            (
                "Cash used by financing activities was $120.6 million in fiscal 2022, compared to $107.9 million in fiscal 2021. In fiscal 2022, we paid dividends totaling $20.3 million and repurchased 2,292,846 shares under our authorized share repurchase program, at a total cost of $100.0 million. We repurchased 1,177,704 shares under the program in fiscal 2021 and 686,997 shares under the program in fiscal 2020. We have repurchased a total of 9,425,462 shares, at a total cost of $307.3 million, since the 2004 inception of this program. We have remaining authority to repurchase 1,824,538 shares under this program, which has no expiration date, and we will continue to evaluate making future share repurchases, depending on our cash flow and debt levels, market conditions, including the continuing effects of the COVID-19 pandemic, and other potential uses of cash.",
                "In fiscal 2022, we paid dividends totaling $20.3 million and repurchased 2,292,846 shares under our authorized share repurchase program, at a total cost of $100.0 million.",
            ),
        ],
    )
    def test_read_returns_match(self, text, expected):
        # assemble
        parser = RepurchaseParser()

        # act
        result = parser.find_best_matches(text)

        # assert
        assert result == expected
