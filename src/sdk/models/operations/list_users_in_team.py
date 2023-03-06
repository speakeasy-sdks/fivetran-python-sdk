from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ListUsersInTeamPathParams:
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListUsersInTeamQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListUsersInTeamHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListUsersInTeamRequest:
    headers: ListUsersInTeamHeaders = dataclasses.field()
    path_params: ListUsersInTeamPathParams = dataclasses.field()
    query_params: ListUsersInTeamQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListUsersInTeamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_users_in_team_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    