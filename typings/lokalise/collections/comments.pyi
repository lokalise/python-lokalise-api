from lokalise.collections.base_collection import BaseCollection
from lokalise.models.comment import CommentModel

class CommentsCollection(BaseCollection[CommentModel]):
    items: list[CommentModel]
