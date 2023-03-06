from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import newdbtprojectrequest as shared_newdbtprojectrequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateDbtProjectHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateDbtProjectRequest:
    headers: CreateDbtProjectHeaders = dataclasses.field()
    request: Optional[shared_newdbtprojectrequest.NewDbtProjectRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateDbtProjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_dbt_project_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    