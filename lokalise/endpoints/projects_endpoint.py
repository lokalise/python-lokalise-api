from .base_endpoint import BaseEndpoint


class ProjectsEndpoint(BaseEndpoint):
    PATH = "projects/{project_id}"
