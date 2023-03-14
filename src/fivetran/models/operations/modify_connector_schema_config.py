from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import standardconfigupdaterequest as shared_standardconfigupdaterequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyConnectorSchemaConfigRequest:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    standard_config_update_request: Optional[shared_standardconfigupdaterequest.StandardConfigUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ModifyConnectorSchemaConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    modify_connector_schema_config_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    