from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import webhookrequest as shared_webhookrequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateGroupWebhookPathParams:
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateGroupWebhookHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateGroupWebhookRequest:
    headers: CreateGroupWebhookHeaders = dataclasses.field()
    path_params: CreateGroupWebhookPathParams = dataclasses.field()
    request: Optional[shared_webhookrequest.WebhookRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateGroupWebhookResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_group_webhook_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    