"""
lokalise.models.base_model
~~~~~~~~~~~~~~~~~~~~~~~~~~
Model parent class inherited by specific models.
"""
from typing import List, Dict


class BaseModel:
    """Abstract base class for model objects.

    :attribute ATTRS: list of attributes a resource contains. For example, a project
    has a name, a description, and an ID.

    :attribute DATA_KEY: contains the key name that should be used to fetch
    data. Response usually arrives in the following format:
    {"project_id": "abc", contributor: {"user_id": 1}}
    In this case, the DATA_KEY would be "contributor"
    """
    ATTRS: List[str] = []
    DATA_KEY = ''

    def __init__(self, raw_data: Dict) -> None:
        """Creates a new model.
        A model describes a single resource,
        for example a project or a contributor. Models respond to common
        methods like `project_id` or `team_id`. To read raw data returned
        by the API, use `raw_data` attribute.

        :param raw_data: Data returned by the API
        """
        self.raw_data = raw_data
        self.branch = raw_data.get('branch', None)

        if 'project_id' not in self.ATTRS:
            self.project_id = raw_data.get('project_id', None)

        # Fetch data with DATA_KEY or simply use the initial data
        data = raw_data.get(self.DATA_KEY, raw_data)

        for attr in self.ATTRS:
            setattr(self, attr, data.get(attr, None))

    def __str__(self) -> str:
        """Converts a model to string
        """
        result = ""
        for attr in self.ATTRS:
            if len(result) != 0:
                result += "\n"
            result += f"{attr}: {getattr(self, attr)}"

        return result
