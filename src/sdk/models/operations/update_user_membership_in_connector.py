from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import updatemembershiprequest as shared_updatemembershiprequest
from typing import Any, Optional


@dataclasses.dataclass
class UpdateUserMembershipInConnectorPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateUserMembershipInConnectorHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateUserMembershipInConnectorRequest:
    headers: UpdateUserMembershipInConnectorHeaders = dataclasses.field()
    path_params: UpdateUserMembershipInConnectorPathParams = dataclasses.field()
    request: Optional[shared_updatemembershiprequest.UpdateMembershipRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateUserMembershipInConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_user_membership_in_connector_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    