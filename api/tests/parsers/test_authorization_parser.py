import pytest

from api.src.parsers.authorization_parser import AuthorizationParser


class TestAuthorizationParser:
    def test_read_returns_na(self):
        # assemble
        text = "no matches here"
        parser = AuthorizationParser()

        # act
        result = parser.find_best_matches(text)

        # assert
        assert result == []

    @pytest.mark.parametrize(
        "text, expected",
        [
            (
                "The following table sets forth the range of high and low closing prices for our common stock for each full quarterly period during fiscal years 2021 and 2020, as reported by the NASDAQ Global Select Market. These quotations below reflect inter-dealer closing prices, without retail mark-up, mark-down, or commission and may not necessarily represent actual transactions. On April 26, 2018, the Company’s Board of Directors authorized a stock repurchase program for up to 500,000 shares of the Company’s stock.  The actual number of shares repurchased and the timing of repurchases will be determined by the Board of Directors and will depend on a number of factors, including stock price, trading volume, general market conditions, working capital requirements, general business conditions, and other factors. The stock repurchase program has no time limit and may be modified, suspended, or terminated at any time.",
                [
                    ". On April 26, 2018, the Company’s Board of Directors authorized a stock "
                    "repurchase program for up to 500,000 shares of the Company’s stock",
                    "s. On April 26, 2018, the Company’s Board of Directors authorized a stock "
                    "repurchase program for up to 500,000 shares of the Company’s stock.  The "
                    "actual number of shares repurchased and the ti",
                ],
            )
        ],
    )
    def test_read_returns_match(self, text, expected):
        # assemble
        parser = AuthorizationParser()

        # act
        result = parser.find_best_matches(text)

        # assert
        assert sorted(result) == sorted(expected)
