from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import teamrequest as shared_teamrequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateTeamHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateTeamRequest:
    headers: CreateTeamHeaders = dataclasses.field()
    request: Optional[shared_teamrequest.TeamRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateTeamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_team_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    