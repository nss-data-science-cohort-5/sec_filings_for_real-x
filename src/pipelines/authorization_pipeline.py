from src.labelers.authorization_labeler import AuthorizationLabeler
from src.labelers.repurchase_labeler import RepurchaseLabeler
from src.parsers.authorization_parser import AuthorizationParser
from src.parsers.repurchase_parser import RepurchaseParser
from src.pipelines.pipeline_protocol import PipelineProtocol
from src.utils.html_reader import HtmlReader


class AuthorizationPipeline(PipelineProtocol):
    def run(self, html: str) -> dict[str, str]:
        parser = AuthorizationParser()
        labeler = AuthorizationLabeler()

        text = HtmlReader.read_text(html)
        text = parser.find_best_matches(text)
        labels = labeler.get_named_entities(text)
        return labels
