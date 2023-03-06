from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DbtProjectDetailsPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'projectId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DbtProjectDetailsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DbtProjectDetailsRequest:
    headers: DbtProjectDetailsHeaders = dataclasses.field()
    path_params: DbtProjectDetailsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DbtProjectDetailsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    dbt_project_details_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    