from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import membershiprequest as shared_membershiprequest
from typing import Any, Optional


@dataclasses.dataclass
class AddTeamMembershipInConnectorPathParams:
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddTeamMembershipInConnectorHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddTeamMembershipInConnectorRequest:
    headers: AddTeamMembershipInConnectorHeaders = dataclasses.field()
    path_params: AddTeamMembershipInConnectorPathParams = dataclasses.field()
    request: Optional[shared_membershiprequest.MembershipRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class AddTeamMembershipInConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    add_team_membership_in_connector_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    