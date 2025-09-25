from lokalise.models.webhook import WebhookModel
from lokalise.collections.base_collection import BaseCollection

class WebhooksCollection(BaseCollection[WebhookModel]):
    items: list[WebhookModel]
