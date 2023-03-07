from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ListAllConnectorsInGroupPathParams:
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListAllConnectorsInGroupQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    schema: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'schema', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListAllConnectorsInGroupHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListAllConnectorsInGroupRequest:
    headers: ListAllConnectorsInGroupHeaders = dataclasses.field()
    path_params: ListAllConnectorsInGroupPathParams = dataclasses.field()
    query_params: ListAllConnectorsInGroupQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListAllConnectorsInGroupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_all_connectors_in_group_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    