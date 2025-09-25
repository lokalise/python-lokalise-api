from lokalise.models.comment import CommentModel
from lokalise.collections.base_collection import BaseCollection

class CommentsCollection(BaseCollection[CommentModel]):
    items: list[CommentModel]
