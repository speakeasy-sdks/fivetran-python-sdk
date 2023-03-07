from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import newtransformationrequest as shared_newtransformationrequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateDbtTransformationPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'projectId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateDbtTransformationHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateDbtTransformationRequest:
    headers: CreateDbtTransformationHeaders = dataclasses.field()
    path_params: CreateDbtTransformationPathParams = dataclasses.field()
    request: Optional[shared_newtransformationrequest.NewTransformationRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateDbtTransformationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_dbt_transformation_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    