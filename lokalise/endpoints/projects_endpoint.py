from .base import Base
from .. import request


class ProjectsEndpoint(Base):
    PATH = "projects"

    def __init__(self, client):
        self.client = client

    def all(self, params={}):
        return request.get(self.client, self.PATH, params)

    def find(self, project_id):
        return request.get(self.client, f"{self.PATH}/{project_id}")
