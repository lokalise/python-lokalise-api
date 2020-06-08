from .base import Base
from .. import request

class ProjectsEndpoint(Base):
    PATH = "projects"
    def __init__(self, client):
        self.client = client

    def all(self):
        return request.get(self.client, self.PATH)
