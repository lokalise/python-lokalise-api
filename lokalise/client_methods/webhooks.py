"""
lokalise.client_methods.webhooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains API client definition for webhooks.
"""

from typing import Any

from lokalise.collections.webhooks import WebhooksCollection
from lokalise.models.webhook import WebhookModel

from .endpoint_provider import EndpointProviderMixin


class WebhookMethods(EndpointProviderMixin):
    """Webhook client methods."""

    def webhooks(
        self, project_id: str, params: dict[str, str | int] | None = None
    ) -> WebhooksCollection:
        """Lists all webhooks set for a project.

        :param str project_id: ID of the project
        :param dict params: Pagination parameters
        :return: Webhook collection
        """
        raw_webhooks = self.get_endpoint("webhooks").all(params=params, parent_id=project_id)
        return WebhooksCollection(raw_webhooks)

    def webhook(self, project_id: str, webhook_id: str) -> WebhookModel:
        """Fetches a webhook.

        :param str project_id: ID of the project
        :param str webhook_id: ID of the webhook to fetch
        :return: Webhook model
        """
        raw_webhook = self.get_endpoint("webhooks").find(
            parent_id=project_id, resource_id=webhook_id
        )
        return WebhookModel(raw_webhook)

    def create_webhook(self, project_id: str, params: dict[str, Any]) -> WebhookModel:
        """Creates a webhook.

        :param str project_id: ID of the project
        :param dict params: Webhook parameters
        :return: Webhook model
        """
        raw_webhook = self.get_endpoint("webhooks").create(params=params, parent_id=project_id)
        return WebhookModel(raw_webhook)

    def update_webhook(
        self, project_id: str, webhook_id: str, params: dict[str, Any] | None = None
    ) -> WebhookModel:
        """Updates a webhook.

        :param str project_id: ID of the project
        :param str webhook_id: ID of the webhook to update
        :param dict params: Webhook parameters
        :return: Webhook model
        """
        raw_webhook = self.get_endpoint("webhooks").update(
            params=params, parent_id=project_id, resource_id=webhook_id
        )
        return WebhookModel(raw_webhook)

    def delete_webhook(self, project_id: str, webhook_id: str) -> dict[str, Any]:
        """Deletes a webhook.

        :param str project_id: ID of the project
        :param str webhook_id: ID of the webhook to delete
        :return: Dict with project ID and `webhook_deleted` set to True
        """
        response = self.get_endpoint("webhooks").delete(
            parent_id=project_id, resource_id=webhook_id
        )
        return response

    def regenerate_webhook_secret(self, project_id: str, webhook_id: str) -> dict[str, Any]:
        """Regenerates a secret key for the webhook.

        :param str project_id: ID of the project
        :param str webhook_id: ID of the webhook to regenerate secret for
        :return: Dict with project ID and `secret` with the new secret's value
        """
        response = self.get_endpoint("webhooks").regenerate_secret(
            parent_id=project_id, resource_id=webhook_id
        )
        return response
