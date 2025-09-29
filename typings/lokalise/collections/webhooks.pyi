from lokalise.collections.base_collection import BaseCollection
from lokalise.models.webhook import WebhookModel

class WebhooksCollection(BaseCollection[WebhookModel]):
    items: list[WebhookModel]
