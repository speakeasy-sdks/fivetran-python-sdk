from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class GetUserMembershipsInGroupsPathParams:
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetUserMembershipsInGroupsQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetUserMembershipsInGroupsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetUserMembershipsInGroupsRequest:
    headers: GetUserMembershipsInGroupsHeaders = dataclasses.field()
    path_params: GetUserMembershipsInGroupsPathParams = dataclasses.field()
    query_params: GetUserMembershipsInGroupsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetUserMembershipsInGroupsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_user_memberships_in_groups_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    