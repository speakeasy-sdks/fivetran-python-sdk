from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import teammembershiprequest as shared_teammembershiprequest
from typing import Any, Optional


@dataclasses.dataclass
class AddUserToTeamPathParams:
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddUserToTeamHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddUserToTeamRequest:
    headers: AddUserToTeamHeaders = dataclasses.field()
    path_params: AddUserToTeamPathParams = dataclasses.field()
    request: Optional[shared_teammembershiprequest.TeamMembershipRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class AddUserToTeamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    add_user_to_team_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    