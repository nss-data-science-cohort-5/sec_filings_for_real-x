import pytest

from api.src.filing_handler import FilingHandler


class TestFilingHandler:
    @pytest.mark.parametrize(
        "filepath, expected",
        [
            (
                "./stubs/reports/cnxc-20211130.htm",
                {
                    "authorized": [
                        {"amount": "up to $500 million", "date": "September 2021"},
                        {"amount": "up to $500,000", "date": "September 2021"},
                    ],
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
                    ],
                },
            ),
            # bww has not made any repurchases
            (
                "./stubs/reports/bbw20220129_10k.html",
                {
                    "authorized": [
                        {"date": "2020", "number": "1,000,000"},
                        {"amount": "$25 million", "date": "November 2021"},
                        {
                            "amount": "$12.9 million",
                            "date": "the fourth quarter of fiscal 2021",
                        },
                    ],
                    "repurchased": [],
                },
            ),
            # TODO: azz should have some results but they're in a table
            (
                "./stubs/reports/azz-20220228.html",
                {
                    "authorized": [
                        {"amount": "$100 million", "date": "November 10, 2020"},
                        {"amount": "$100.0 million", "date": "November 10, 2020"},
                    ],
                    "repurchased": [],
                },
            ),
            (
                "./stubs/reports/apog-20220226.html",
                {
                    "authorized": [
                        {"date": "April 10, 2003", "number": "1,500,000"},
                        {"date": "January 24, 2008", "number": "0,000"},
                        {"date": "fiscal 2004", "number": "2,292,846"},
                    ],
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
                    ],
                },
            ),
            (
                "./stubs/reports/amrk-10k_20210630.htm",
                {
                    "authorized": [
                        {"date": "April 26, 2018", "number": "up to 500,000"}
                    ],
                    "repurchased": [],
                },
            ),
            (
                "./stubs/reports/fnhc-20211231.html",
                {
                    "authorized": [
                        {"amount": "an additional $10.0 million", "date": "2020"},
                        {"amount": "up to $10.0 million", "date": "December 2018"},
                        {"amount": "up to $20 million", "date": "December 31, 2020"},
                        {"amount": "an additional $10.0 million", "date": "March 2020"},
                    ],
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
                    ],
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
