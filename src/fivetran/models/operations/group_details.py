from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class GroupDetailsPathParams:
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GroupDetailsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GroupDetailsRequest:
    headers: GroupDetailsHeaders = dataclasses.field()
    path_params: GroupDetailsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GroupDetailsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    group_details_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    