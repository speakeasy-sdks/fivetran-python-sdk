from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DeleteTeamMembershipInConnectorPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteTeamMembershipInConnectorHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteTeamMembershipInConnectorRequest:
    headers: DeleteTeamMembershipInConnectorHeaders = dataclasses.field()
    path_params: DeleteTeamMembershipInConnectorPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteTeamMembershipInConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_team_membership_in_connector_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    