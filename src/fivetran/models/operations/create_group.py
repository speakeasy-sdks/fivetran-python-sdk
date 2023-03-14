from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import newgrouprequest as shared_newgrouprequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateGroupRequest:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    new_group_request: Optional[shared_newgrouprequest.NewGroupRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateGroupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_group_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    