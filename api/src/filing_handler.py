from api.src.pipelines.authorization_pipeline import AuthorizationPipeline
from api.src.pipelines.repurchase_pipeline import RepurchasePipeline


class FilingHandler:
    @classmethod
    def handle(cls, html: str) -> dict[str, dict[str, str]]:
        authorization_info = AuthorizationPipeline().run(html)
        repurchase_info = RepurchasePipeline().run(html)
        return {"authorized": authorization_info, "repurchased": repurchase_info}
