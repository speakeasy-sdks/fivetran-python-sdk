from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import reloadstandardconfigrequest as shared_reloadstandardconfigrequest
from typing import Any, Optional


@dataclasses.dataclass
class ReloadConnectorSchemaConfigRequest:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    reload_standard_config_request: Optional[shared_reloadstandardconfigrequest.ReloadStandardConfigRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ReloadConnectorSchemaConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    reload_connector_schema_config_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    