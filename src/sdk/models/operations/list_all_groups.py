from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ListAllGroupsQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListAllGroupsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListAllGroupsRequest:
    headers: ListAllGroupsHeaders = dataclasses.field()
    query_params: ListAllGroupsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListAllGroupsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_all_groups_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    