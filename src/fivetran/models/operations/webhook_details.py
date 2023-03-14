from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class WebhookDetailsRequest:
    webhook_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'webhookId', 'style': 'simple', 'explode': False }})
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class WebhookDetailsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    webhook_details_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    