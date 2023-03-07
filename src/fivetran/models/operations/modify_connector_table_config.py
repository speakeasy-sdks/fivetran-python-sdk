from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import tableupdaterequest as shared_tableupdaterequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyConnectorTableConfigPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    schema_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'schemaName', 'style': 'simple', 'explode': False }})
    table_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tableName', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyConnectorTableConfigHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ModifyConnectorTableConfigRequest:
    headers: ModifyConnectorTableConfigHeaders = dataclasses.field()
    path_params: ModifyConnectorTableConfigPathParams = dataclasses.field()
    request: Optional[shared_tableupdaterequest.TableUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ModifyConnectorTableConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    modify_connector_table_config_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    