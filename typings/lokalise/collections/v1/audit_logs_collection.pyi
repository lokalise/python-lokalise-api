from lokalise.collections.v1.base_collection import BaseCollectionV1
from lokalise.models.v1.audit_log import AuditLogModel

class AuditLogsCollection(BaseCollectionV1[AuditLogModel]):
    items: list[AuditLogModel]
