from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import newuserrequest as shared_newuserrequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateUserHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateUserRequest:
    headers: CreateUserHeaders = dataclasses.field()
    request: Optional[shared_newuserrequest.NewUserRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateUserResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_user_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    