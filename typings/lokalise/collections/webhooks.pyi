from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.webhook import WebhookModel

class WebhooksCollection(ExpertCollection[WebhookModel]):
    items: list[WebhookModel]
