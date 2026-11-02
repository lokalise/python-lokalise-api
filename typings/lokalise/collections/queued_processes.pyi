from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.queued_process import QueuedProcessModel

class QueuedProcessesCollection(ExpertCollection[QueuedProcessModel]):
    items: list[QueuedProcessModel]
