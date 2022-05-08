import pytest
from src.labelers.repurchase_labeler import RepurchaseLabeler


class TestRepurchaseLabeler:
    @pytest.mark.parametrize(
        "text, expected",
        [
            (
                "During the fiscal year ended July 31, 2021, the Company repurchased 1,488,991 shares of common stock at an average price of $109.17 per share, for an aggregate purchase price of $162.5 million. ",
                {
                    "date": "the fiscal year ended July 31, 2021",
                    "number": "1,488,991",
                    "amount": "$162.5 million",
                },
            )
        ],
    )
    def test_apply_labels(self, text, expected):
        # assemble
        labeler = RepurchaseLabeler()

        # act
        result = labeler.get_named_entities(text)

        # assert
        assert expected == result
