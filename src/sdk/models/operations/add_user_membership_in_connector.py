from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import membershiprequest as shared_membershiprequest
from ..shared import membershipresponse as shared_membershipresponse
from typing import Optional


@dataclasses.dataclass
class AddUserMembershipInConnectorPathParams:
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddUserMembershipInConnectorHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddUserMembershipInConnectorRequest:
    headers: AddUserMembershipInConnectorHeaders = dataclasses.field()
    path_params: AddUserMembershipInConnectorPathParams = dataclasses.field()
    request: Optional[shared_membershiprequest.MembershipRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class AddUserMembershipInConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    membership_response: Optional[shared_membershipresponse.MembershipResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    