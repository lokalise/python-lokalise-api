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

    :attribute COMMON_ATTRS: list of common attributes that the models may have.
    For example: project_id, user_id, branch, team_id.

    :attribute DATA_KEY: contains the key name that should be used to fetch
    data. Response usually arrives in the following format:
    {"project_id": "abc", contributor: {"user_id": 1}}
    In this case, the DATA_KEY would be "contributor"
    """
    ATTRS: List[str] = []
    COMMON_ATTRS: List[str] = [
        'project_id',
        'user_id',
        'branch'
    ]
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
        self.__extract_common_attrs(raw_data)

        # Fetch data with DATA_KEY or simply use the initial data.
        # In some cases the DATA_KEY is the same as the object attribute.
        # For example:
        # "comments": [{
        #     "comment_id": 44444,
        #     "comment": "Hello, world!"
        # }]
        # This object has a `comment` attribute but its DATA_KEY is also `comment`:
        # "comment": {"comment_id": 44444,
        #     "key_id": 12345,
        #     "comment": "This is a test."}
        # This is an edge case happening only twice, so to overcome it
        # just check the value type under the given key.
        if self.DATA_KEY in raw_data and \
                (isinstance(raw_data[self.DATA_KEY], dict)):
            data = raw_data[self.DATA_KEY]
        else:
            data = raw_data

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

    def __extract_common_attrs(self, raw_data: Dict) -> None:
        """Fetches common data from the response and sets the
        corresponding attributes. If the same attribute is present in model-specific
        attribute list, it has higher priority.
        """
        for attr in self.COMMON_ATTRS:
            if attr not in self.ATTRS and attr in raw_data:
                setattr(self, attr, raw_data[attr])
