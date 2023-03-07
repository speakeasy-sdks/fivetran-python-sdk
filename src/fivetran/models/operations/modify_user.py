from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import updateuserrequest as shared_updateuserrequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyUserPathParams:
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyUserHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyUserRequest:
    headers: ModifyUserHeaders = dataclasses.field()
    path_params: ModifyUserPathParams = dataclasses.field()
    request: Optional[shared_updateuserrequest.UpdateUserRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ModifyUserResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    modify_user_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    