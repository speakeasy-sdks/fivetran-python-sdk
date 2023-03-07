from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class GetUserMembershipsInConnectorsPathParams:
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetUserMembershipsInConnectorsQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetUserMembershipsInConnectorsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetUserMembershipsInConnectorsRequest:
    headers: GetUserMembershipsInConnectorsHeaders = dataclasses.field()
    path_params: GetUserMembershipsInConnectorsPathParams = dataclasses.field()
    query_params: GetUserMembershipsInConnectorsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetUserMembershipsInConnectorsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_user_memberships_in_connectors_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    