from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import membershiprequest as shared_membershiprequest
from typing import Any, Optional


@dataclasses.dataclass
class AddUserMembershipInGroupPathParams:
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddUserMembershipInGroupHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddUserMembershipInGroupRequest:
    headers: AddUserMembershipInGroupHeaders = dataclasses.field()
    path_params: AddUserMembershipInGroupPathParams = dataclasses.field()
    request: Optional[shared_membershiprequest.MembershipRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class AddUserMembershipInGroupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    add_user_membership_in_group_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    