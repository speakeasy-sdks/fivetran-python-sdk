from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class GetUserInTeamPathParams:
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetUserInTeamHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetUserInTeamRequest:
    headers: GetUserInTeamHeaders = dataclasses.field()
    path_params: GetUserInTeamPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetUserInTeamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_user_in_team_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    