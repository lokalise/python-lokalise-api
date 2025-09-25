from lokalise.models.permission_template import PermissionTemplateModel
from lokalise.collections.base_collection import BaseCollection

class PermissionTemplatesCollection(BaseCollection[PermissionTemplateModel]):
    items: list[PermissionTemplateModel]
