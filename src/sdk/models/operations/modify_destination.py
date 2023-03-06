from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import updatedestinationrequest as shared_updatedestinationrequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyDestinationPathParams:
    destination_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'destinationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyDestinationHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyDestinationRequest:
    headers: ModifyDestinationHeaders = dataclasses.field()
    path_params: ModifyDestinationPathParams = dataclasses.field()
    request: Optional[shared_updatedestinationrequest.UpdateDestinationRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ModifyDestinationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    modify_destination_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    