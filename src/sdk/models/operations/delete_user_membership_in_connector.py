from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DeleteUserMembershipInConnectorPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteUserMembershipInConnectorHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteUserMembershipInConnectorRequest:
    headers: DeleteUserMembershipInConnectorHeaders = dataclasses.field()
    path_params: DeleteUserMembershipInConnectorPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteUserMembershipInConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_user_membership_in_connector_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    