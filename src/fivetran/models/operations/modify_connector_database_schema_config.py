from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import schemaupdaterequest as shared_schemaupdaterequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyConnectorDatabaseSchemaConfigPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    schema_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'schemaName', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyConnectorDatabaseSchemaConfigHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyConnectorDatabaseSchemaConfigRequest:
    headers: ModifyConnectorDatabaseSchemaConfigHeaders = dataclasses.field()
    path_params: ModifyConnectorDatabaseSchemaConfigPathParams = dataclasses.field()
    request: Optional[shared_schemaupdaterequest.SchemaUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ModifyConnectorDatabaseSchemaConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    modify_connector_database_schema_config_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    