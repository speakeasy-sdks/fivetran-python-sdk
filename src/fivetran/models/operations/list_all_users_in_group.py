from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ListAllUsersInGroupPathParams:
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListAllUsersInGroupQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListAllUsersInGroupHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListAllUsersInGroupRequest:
    headers: ListAllUsersInGroupHeaders = dataclasses.field()
    path_params: ListAllUsersInGroupPathParams = dataclasses.field()
    query_params: ListAllUsersInGroupQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListAllUsersInGroupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_all_users_in_group_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    