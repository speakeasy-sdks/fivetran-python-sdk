from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import teamrequest as shared_teamrequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyTeamPathParams:
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyTeamHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyTeamRequest:
    headers: ModifyTeamHeaders = dataclasses.field()
    path_params: ModifyTeamPathParams = dataclasses.field()
    request: Optional[shared_teamrequest.TeamRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ModifyTeamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    modify_team_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    