from lokalise.collections.expert_collection import ExpertCollection
from lokalise.models.comment import CommentModel

class CommentsCollection(ExpertCollection[CommentModel]):
    items: list[CommentModel]
