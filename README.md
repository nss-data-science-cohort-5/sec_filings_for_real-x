# SEC Filings Automated Data Extraction

In this project, your objective is to produce a method of automatically extracting information from a company's 10-K filing. The 10-K is a required annual report that gives a comprehensive overview of the company's business and financial condition. Your specific goal is to extract information a company's share repurchases. A share repurchase is a transaction where a company buys back its own shares from the marketplace.

You have been provided with 30 10-K forms in HTML format along with annotations for the relevant text and values.

These (and other) filings can be retrieved from [EDGAR, the Electronic Data Gathering, Analysis, and Retrieval system](https://www.sec.gov/edgar/search-and-access). You can test out how well your processing pipeline works on new filings by downloading additional 10-K forms from here.

There are three major components to this project, and your final product will combine these three components into one pipeline for processing 10-K forms.

1. You have been provided these filings in HTML format. Your first task is to find a way to read these into Python and prepare them for further processing. (Hint: BeautifulSoup might be useful here).
2. There is not a specific format 10-K forms must adhere to, and as a result, there is not a standard location for stock repurchase information. The second component of this project is to identify the paragraphs or sections of each filing that contain this information. Build a text classifier (or use some other method) to identifies paragraphs, sentences, or blocks of text that are likely to be relevant to the task of extracting share repurchase information.
3. After identifying relevant pieces of text, you need to extract the share repurchase information from the paragraphs.

Your final product should allow you to input a 10-K filing as an HTML file and produce a list of relevant information on stock repurchases (or lack thereof).

The fields that you are looking to extract are as follows:
* authorization_date: When was the repurchase authorized?
* authorization_amount: Dollar amount of repurchases authorized
* authorization_number: Number of repurchase shares authorized
* repurchase_date: When did the repurchase occur?
* repurchase_amount: Dollar amount of repurchases
* repurchase_number: Number of shares repurchased

Note that a filing may have multiple annotations and a given paragraph or sentence may even have multiple annotations. Also, make note that the annotations you have received are imperfect but can be used as a starting point to build your information extractor.