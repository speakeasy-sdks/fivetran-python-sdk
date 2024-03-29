"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import updateuserrequest as shared_updateuserrequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyUserRequest:
    
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the user within the account."""  
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    update_user_request: Optional[shared_updateuserrequest.UpdateUserRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class ModifyUserResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    modify_user_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    