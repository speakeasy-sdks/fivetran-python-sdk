"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import groupresponse as shared_groupresponse
from ..shared import updategrouprequest as shared_updategrouprequest
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclasses.dataclass
class ModifyGroupRequest:
    
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the group within the Fivetran system."""
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    update_group_request: Optional[shared_updategrouprequest.UpdateGroupRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModifyGroup200ApplicationJSON:
    r"""Successful response"""
    
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""Response status code"""
    data: Optional[shared_groupresponse.GroupResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""Response status text"""
    

@dataclasses.dataclass
class ModifyGroupResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    modify_group_200_application_json_object: Optional[ModifyGroup200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    