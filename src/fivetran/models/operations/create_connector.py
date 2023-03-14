from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import newconnectorrequestv1 as shared_newconnectorrequestv1
from typing import Any, Optional


@dataclasses.dataclass
class CreateConnectorRequest:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    new_connector_request_v1: Optional[shared_newconnectorrequestv1.NewConnectorRequestV1] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_connector_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    