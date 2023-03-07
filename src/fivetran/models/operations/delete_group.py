from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DeleteGroupPathParams:
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteGroupHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteGroupRequest:
    headers: DeleteGroupHeaders = dataclasses.field()
    path_params: DeleteGroupPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteGroupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_group_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    