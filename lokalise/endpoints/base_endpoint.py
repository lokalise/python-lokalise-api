from .. import request


class BaseEndpoint:
    PATH = ''
    def __init__(self, client):
        self.client = client

    def all(self, project_id=None, params={}):
        path = self.PATH.format(
            project_id=project_id if project_id else "",
            resource_id=""
        ).strip('/')
        return request.get(self.client, path, params)

    def find(self, project_id, resource_id=None):
        path = self.PATH.format(
            project_id=project_id,
            resource_id=resource_id if resource_id else ""
        ).strip('/')
        return request.get(self.client, path)
