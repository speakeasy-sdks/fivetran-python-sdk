"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import addusertogrouprequest as shared_addusertogrouprequest
from typing import Any, Optional


@dataclasses.dataclass
class AddUserToGroupRequest:
    
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the group within the Fivetran system."""  
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    add_user_to_group_request: Optional[shared_addusertogrouprequest.AddUserToGroupRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class AddUserToGroupResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    add_user_to_group_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    