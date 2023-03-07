from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DeleteConnectorPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteConnectorHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteConnectorRequest:
    headers: DeleteConnectorHeaders = dataclasses.field()
    path_params: DeleteConnectorPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_connector_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    