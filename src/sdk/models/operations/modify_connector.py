from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import updateconnectorrequest as shared_updateconnectorrequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyConnectorPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyConnectorHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyConnectorRequest:
    headers: ModifyConnectorHeaders = dataclasses.field()
    path_params: ModifyConnectorPathParams = dataclasses.field()
    request: Optional[shared_updateconnectorrequest.UpdateConnectorRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ModifyConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    modify_connector_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    