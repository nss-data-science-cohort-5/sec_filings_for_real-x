from src.pipelines.repurchase_pipeline import RepurchasePipeline


class FilingHandler:
    @classmethod
    def handle(cls, html: str) -> dict[str, dict[str, str]]:
        repurchase_info = RepurchasePipeline().run(html)
        return {"repurchased": repurchase_info}
