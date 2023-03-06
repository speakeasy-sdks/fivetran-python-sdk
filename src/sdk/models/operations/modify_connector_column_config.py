from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import columnupdaterequest as shared_columnupdaterequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyConnectorColumnConfigPathParams:
    column_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'columnName', 'style': 'simple', 'explode': False }})
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    schema_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'schemaName', 'style': 'simple', 'explode': False }})
    table_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tableName', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyConnectorColumnConfigHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyConnectorColumnConfigRequest:
    headers: ModifyConnectorColumnConfigHeaders = dataclasses.field()
    path_params: ModifyConnectorColumnConfigPathParams = dataclasses.field()
    request: Optional[shared_columnupdaterequest.ColumnUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ModifyConnectorColumnConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    modify_connector_column_config_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    