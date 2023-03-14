from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import webhooktestrequest as shared_webhooktestrequest
from typing import Any, Optional


@dataclasses.dataclass
class TestWebhookRequest:
    webhook_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'webhookId', 'style': 'simple', 'explode': False }})
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    webhook_test_request: Optional[shared_webhooktestrequest.WebhookTestRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TestWebhookResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    test_webhook_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    