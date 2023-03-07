from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class TestDbtProjectPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'projectId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TestDbtProjectHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TestDbtProjectRequest:
    headers: TestDbtProjectHeaders = dataclasses.field()
    path_params: TestDbtProjectPathParams = dataclasses.field()
    

@dataclasses.dataclass
class TestDbtProjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    test_dbt_project_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    