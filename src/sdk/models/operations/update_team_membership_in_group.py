from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import updatemembershiprequest as shared_updatemembershiprequest
from typing import Any, Optional


@dataclasses.dataclass
class UpdateTeamMembershipInGroupPathParams:
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateTeamMembershipInGroupHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateTeamMembershipInGroupRequest:
    headers: UpdateTeamMembershipInGroupHeaders = dataclasses.field()
    path_params: UpdateTeamMembershipInGroupPathParams = dataclasses.field()
    request: Optional[shared_updatemembershiprequest.UpdateMembershipRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateTeamMembershipInGroupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_team_membership_in_group_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    