from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import syncconnectorrequest as shared_syncconnectorrequest
from typing import Any, Optional


@dataclasses.dataclass
class SyncConnectorPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SyncConnectorHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SyncConnectorRequest:
    headers: SyncConnectorHeaders = dataclasses.field()
    path_params: SyncConnectorPathParams = dataclasses.field()
    request: Optional[shared_syncconnectorrequest.SyncConnectorRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SyncConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    sync_connector_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    