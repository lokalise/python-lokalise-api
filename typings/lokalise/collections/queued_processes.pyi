from lokalise.models.queued_process import QueuedProcessModel
from lokalise.collections.base_collection import BaseCollection

class QueuedProcessesCollection(BaseCollection[QueuedProcessModel]):
    items: list[QueuedProcessModel]
