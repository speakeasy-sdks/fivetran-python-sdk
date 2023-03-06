from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ConnectorSchemaConfigPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ConnectorSchemaConfigHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ConnectorSchemaConfigRequest:
    headers: ConnectorSchemaConfigHeaders = dataclasses.field()
    path_params: ConnectorSchemaConfigPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ConnectorSchemaConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connector_schema_config_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    