from ..models.project import ProjectModel

class ProjectsCollection:
    DATA_KEY = "projects"

    def __init__(self, raw_data):
        raw_items = raw_data[self.DATA_KEY]
        self.items = []
        for item in raw_items: self.items.append(ProjectModel(item))

        pagination = raw_data.get("_pagination", {})
        if pagination:
            self.total_count = pagination.get("x-pagination-total-count", 0)
            self.page_count = pagination.get("x-pagination-page-count", 0)
            self.limit = pagination.get("x-pagination-limit", 0)
            self.current_page = pagination.get("x-pagination-page", 0)
