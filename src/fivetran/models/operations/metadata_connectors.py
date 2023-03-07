from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class MetadataConnectorsPathParams:
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class MetadataConnectorsQueryParams:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class MetadataConnectorsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class MetadataConnectorsRequest:
    headers: MetadataConnectorsHeaders = dataclasses.field()
    path_params: MetadataConnectorsPathParams = dataclasses.field()
    query_params: MetadataConnectorsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class MetadataConnectorsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    metadata_connectors_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    