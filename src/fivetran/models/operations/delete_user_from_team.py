from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DeleteUserFromTeamPathParams:
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteUserFromTeamHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteUserFromTeamRequest:
    headers: DeleteUserFromTeamHeaders = dataclasses.field()
    path_params: DeleteUserFromTeamPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteUserFromTeamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_user_from_team_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    