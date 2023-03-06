from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class MetadataConnectorConfigPathParams:
    name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'name', 'style': 'simple', 'explode': False }})
    service: str = dataclasses.field(metadata={'path_param': { 'field_name': 'service', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class MetadataConnectorConfigHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class MetadataConnectorConfigRequest:
    headers: MetadataConnectorConfigHeaders = dataclasses.field()
    path_params: MetadataConnectorConfigPathParams = dataclasses.field()
    

@dataclasses.dataclass
class MetadataConnectorConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    metadata_connector_config_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    