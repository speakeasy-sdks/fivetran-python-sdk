from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import webhookrequest as shared_webhookrequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateAccountWebhookHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateAccountWebhookRequest:
    headers: CreateAccountWebhookHeaders = dataclasses.field()
    request: Optional[shared_webhookrequest.WebhookRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateAccountWebhookResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_account_webhook_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    