from .base_endpoint import BaseEndpoint


class ContributorsEndpoint(BaseEndpoint):
    PATH = "projects/{project_id}/contributors/{resource_id}"
