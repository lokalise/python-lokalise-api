from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.permission_template import PermissionTemplateModel

class PermissionTemplatesCollection(ExpertCollection[PermissionTemplateModel]):
    items: list[PermissionTemplateModel]
