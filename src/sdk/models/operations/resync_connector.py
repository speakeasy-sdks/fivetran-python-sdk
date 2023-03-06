from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import resyncconnectorrequest as shared_resyncconnectorrequest
from typing import Any, Optional


@dataclasses.dataclass
class ResyncConnectorPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ResyncConnectorHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ResyncConnectorRequest:
    headers: ResyncConnectorHeaders = dataclasses.field()
    path_params: ResyncConnectorPathParams = dataclasses.field()
    request: Optional[shared_resyncconnectorrequest.ResyncConnectorRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ResyncConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    resync_connector_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    