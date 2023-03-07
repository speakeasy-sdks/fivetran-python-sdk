from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DestinationDetailsPathParams:
    destination_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'destinationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DestinationDetailsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DestinationDetailsRequest:
    headers: DestinationDetailsHeaders = dataclasses.field()
    path_params: DestinationDetailsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DestinationDetailsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    destination_details_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    