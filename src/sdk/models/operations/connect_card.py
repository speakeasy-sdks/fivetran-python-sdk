from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectcardconfigrequest as shared_connectcardconfigrequest
from typing import Any, Optional


@dataclasses.dataclass
class ConnectCardPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ConnectCardHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ConnectCardRequest:
    headers: ConnectCardHeaders = dataclasses.field()
    path_params: ConnectCardPathParams = dataclasses.field()
    request: Optional[shared_connectcardconfigrequest.ConnectCardConfigRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ConnectCardResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connect_card_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    