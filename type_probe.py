from lokalise.models.base_model import BaseModel
from lokalise.models.v1.audit_log import AuditLogModel

from lokalise.collections.base_collection import BaseCollection
from lokalise.collections.v1.base_collection import BaseCollectionV1


# 1. Does Pyright recognize the model inheritance?
model: BaseModel = AuditLogModel({})
model_class: type[BaseModel] = AuditLogModel


# 2. Does the generic base collection accept the model?
class TestBaseCollection(BaseCollection[AuditLogModel]):
    pass


# 3. Does the v1 collection accept the model?
class TestV1Collection(BaseCollectionV1[AuditLogModel]):
    pass


reveal_type(AuditLogModel)
reveal_type(BaseModel)