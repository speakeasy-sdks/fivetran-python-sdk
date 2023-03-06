from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class GetUserMembershipInGroupPathParams:
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetUserMembershipInGroupHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetUserMembershipInGroupRequest:
    headers: GetUserMembershipInGroupHeaders = dataclasses.field()
    path_params: GetUserMembershipInGroupPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetUserMembershipInGroupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_user_membership_in_group_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    