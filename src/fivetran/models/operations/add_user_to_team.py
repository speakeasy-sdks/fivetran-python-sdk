"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import teammembershiprequest as shared_teammembershiprequest
from typing import Any, Optional


@dataclasses.dataclass
class AddUserToTeamRequest:
    
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the team within the account"""  
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    team_membership_request: Optional[shared_teammembershiprequest.TeamMembershipRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class AddUserToTeamResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    add_user_to_team_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    