from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ConnectorColumnConfigPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    schema: str = dataclasses.field(metadata={'path_param': { 'field_name': 'schema', 'style': 'simple', 'explode': False }})
    table: str = dataclasses.field(metadata={'path_param': { 'field_name': 'table', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ConnectorColumnConfigHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ConnectorColumnConfigRequest:
    headers: ConnectorColumnConfigHeaders = dataclasses.field()
    path_params: ConnectorColumnConfigPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ConnectorColumnConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connector_column_config_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    