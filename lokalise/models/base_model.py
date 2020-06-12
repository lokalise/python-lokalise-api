"""
lokalise.models.base_model
~~~~~~~~~~~~~~~~~~~~~~~~~~
Model parent class inherited by specific models.
"""

from abc import ABC


class BaseModel(ABC):
    """Abstract base class for model objects.

    :attribute ATTRS: list of attributes a resource contains. For example, a project
    has a name, a description, and an ID.

    :attribute DATA_KEY: contains the key name that should be used to fetch
    data. Response usually arrives in the following format:
    {"project_id": "abc", contributor: {"user_id": 1}}
    In this case, the DATA_KEY would be "contributor"
    """
    ATTRS = []
    DATA_KEY = ''

    def __init__(self, raw_data):
        """Creates a new model.
        A model describes a single resource,
        for example a project or a contributor. Models respond to common
        methods like `project_id` or `team_id`. To read raw data returned
        by the API, use `raw_data` attribute.

        :param raw_data: Data returned by the API
        """
        self.raw_data = raw_data
        if 'project_id' not in self.ATTRS:
            self.project_id = raw_data.get('project_id', None)

        for attr in self.ATTRS:
            if hasattr(self, 'DATA_KEY'):
                raw_data = raw_data.get(self.DATA_KEY, raw_data)
            setattr(self, attr, raw_data.get(attr, None))

    def __str__(self):
        """Converts a model to string
        """
        result = ""
        for attr in self.ATTRS:
            if len(result) != 0:
                result += "\n"
            result += f"{attr}: {getattr(self, attr)}"

        return result
