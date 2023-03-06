from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ListDbtProjectTransformationsPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'projectId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListDbtProjectTransformationsQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListDbtProjectTransformationsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListDbtProjectTransformationsRequest:
    headers: ListDbtProjectTransformationsHeaders = dataclasses.field()
    path_params: ListDbtProjectTransformationsPathParams = dataclasses.field()
    query_params: ListDbtProjectTransformationsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListDbtProjectTransformationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_dbt_project_transformations_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    