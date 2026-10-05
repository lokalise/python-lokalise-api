"""
lokalise.models.base_model
~~~~~~~~~~~~~~~~~~~~~~~~~~
Model parent class inherited by specific models.
"""

from typing import Any, ClassVar, cast


class BaseModel:
    """Abstract base class for model objects.

    :attribute ATTRS: list of attributes a resource contains. For example, a project
    has a name, a description, and an ID.

    :attribute COMMON_ATTRS: list of common attributes that the models may have.

    :attribute DATA_KEY: contains the key name that should be used to fetch
    data. Response usually arrives in the following format:
    {"project_id": "abc", contributor: {"user_id": 1}}
    In this case, the DATA_KEY would be "contributor"
    """

    ATTRS: ClassVar[tuple[str, ...]] = ()
    COMMON_ATTRS: ClassVar[tuple[str, ...]] = (
        "project_id",
        "user_id",
        "branch",
        "team_id",
    )
    DATA_KEY: ClassVar[str] = ""

    raw_data: dict[str, Any]

    project_id: str | None = None
    user_id: int | None = None
    branch: str | None = None
    team_id: int | None = None

    def __init__(self, raw_data: dict[str, Any]) -> None:
        """Creates a new model.
        A model describes a single resource, for example a project or a contributor.
        To read raw data returned by the API, use the `raw_data` attribute.

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
        nested_data = raw_data.get(self.DATA_KEY)

        if isinstance(nested_data, dict):
            data = cast(dict[str, Any], nested_data)
        else:
            data = raw_data

        for attr in self.ATTRS:
            setattr(self, attr, data.get(attr))

    def __str__(self) -> str:
        """Converts a model to string"""
        return "\n".join(f"{attr}: {getattr(self, attr)}" for attr in self.ATTRS)

    def __extract_common_attrs(self, raw_data: dict[str, Any]) -> None:
        """Fetches common data from the response and sets the
        corresponding attributes. If the same attribute is present in model-specific
        attribute list, it has higher priority.
        """
        for attr in self.COMMON_ATTRS:
            if attr not in self.ATTRS and attr in raw_data:
                setattr(self, attr, raw_data[attr])
