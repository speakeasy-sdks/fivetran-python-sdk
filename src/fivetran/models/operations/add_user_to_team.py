"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import teammembershiprequest as shared_teammembershiprequest
from ..shared import teammembershipresponse as shared_teammembershipresponse
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclasses.dataclass
class AddUserToTeamRequest:
    
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the team within the account"""  
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    team_membership_request: Optional[shared_teammembershiprequest.TeamMembershipRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddUserToTeam201ApplicationJSON:
    r"""Successful response"""
    
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""Response status code"""  
    data: Optional[shared_teammembershipresponse.TeamMembershipResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})  
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""Response status text"""  
    

@dataclasses.dataclass
class AddUserToTeamResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    add_user_to_team_201_application_json_object: Optional[AddUserToTeam201ApplicationJSON] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    