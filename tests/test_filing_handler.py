import pytest

from src.filing_handler import FilingHandler


class TestFilingHandler:
    @pytest.mark.parametrize(
        "filepath, expected",
        [
            (
                "./stubs/reports/cnxc-20211130.htm",
                {
                    "repurchased": [
                        {
                            "amount": "approximately $25.1 million",
                            "date": "November 30, 2021",
                            "number": "138,455",
                        },
                        {
                            "amount": "$25.1 million",
                            "date": "l year ended November 30, 2021",
                            "number": "138,455",
                        },
                    ]
                },
            ),
            # bww has not made any repurchases
            ("./stubs/reports/bbw20220129_10k.html", {"repurchased": []}),
            # TODO: azz should have some results but they're in a table
            ("./stubs/reports/azz-20220228.html", {"repurchased": []}),
            (
                "./stubs/reports/apog-20220226.html",
                {
                    "repurchased": [
                        {
                            "amount": "$307.3 million",
                            "date": "2004",
                            "number": "9,425,462",
                        },
                        {
                            "amount": "$307.3 million",
                            "date": "fiscal 2020",
                            "number": "9,425,462",
                        },
                        {
                            "amount": "$100.0 million",
                            "date": "fiscal 2021",
                            "number": "1,177,704",
                        },
                        {
                            "amount": "$32.9 million",
                            "date": "fiscal 2021",
                            "number": "1,177,704",
                        },
                        {
                            "amount": "$100.0 million",
                            "date": "fiscal 2022",
                            "number": "2,292,846",
                        },
                    ]
                },
            ),
            ("./stubs/reports/amrk-10k_20210630.htm", {"repurchased": []}),
            (
                "./stubs/reports/fnhc-20211231.html",
                {
                    "repurchased": [
                        {
                            "amount": "$3.9 million",
                            "date": "December 31, 2019",
                            "number": "237,647",
                        },
                        {
                            "amount": "$10.0 million",
                            "date": "December 31, 2020",
                            "number": "800,235",
                        },
                    ]
                },
            ),
        ],
    )
    def test_handle(self, filepath, expected):
        # assemble
        with open(filepath) as f:
            html = f.read()

        # act
        result = FilingHandler.handle(html)

        # assert
        assert result == expected
