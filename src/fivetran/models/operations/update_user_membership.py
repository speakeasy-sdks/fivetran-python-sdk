from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import updatemembershiprequest as shared_updatemembershiprequest
from typing import Any, Optional


@dataclasses.dataclass
class UpdateUserMembershipRequest:
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    update_membership_request: Optional[shared_updatemembershiprequest.UpdateMembershipRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateUserMembershipResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_user_membership_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    