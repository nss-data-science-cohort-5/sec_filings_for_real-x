import pytest

from api.src.labelers.authorization_labeler import AuthorizationLabeler


class TestAuthorizationLabeler:
    @pytest.mark.parametrize(
        "text, expected",
        [
            (
                [
                    ". On April 26, 2018, the Company’s Board of Directors authorized a stock repurchase program for up to 500,000 shares of the Company’s stock.  The actual number of shares repurchased and the ti"
                ],
                [
                    {
                        "date": "April 26, 2018",
                        "number": "up to 500,000",
                    }
                ],
            ),
            #
            (
                [
                    ". On April 26, 2018, under the Company’s Board of Directors authorized a stock repurchase program, 500,000 shares of the Company’s stock were repurchased for $6 million.  The actual number of shares repurchased and the ti"
                ],
                [],
            ),
        ],
    )
    def test_apply_labels(self, text, expected):
        # assemble
        labeler = AuthorizationLabeler()

        # act
        result = labeler.get_named_entities(text)

        # assert
        assert result == expected
