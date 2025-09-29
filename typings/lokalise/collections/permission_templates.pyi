from lokalise.collections.base_collection import BaseCollection
from lokalise.models.permission_template import PermissionTemplateModel

class PermissionTemplatesCollection(BaseCollection[PermissionTemplateModel]):
    items: list[PermissionTemplateModel]
