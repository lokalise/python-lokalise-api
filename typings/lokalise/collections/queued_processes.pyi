from lokalise.collections.base_collection import BaseCollection
from lokalise.models.queued_process import QueuedProcessModel

class QueuedProcessesCollection(BaseCollection[QueuedProcessModel]):
    items: list[QueuedProcessModel]
