from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class GetTeamMembershipsInGroupsPathParams:
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetTeamMembershipsInGroupsQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetTeamMembershipsInGroupsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetTeamMembershipsInGroupsRequest:
    headers: GetTeamMembershipsInGroupsHeaders = dataclasses.field()
    path_params: GetTeamMembershipsInGroupsPathParams = dataclasses.field()
    query_params: GetTeamMembershipsInGroupsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetTeamMembershipsInGroupsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_team_memberships_in_groups_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    