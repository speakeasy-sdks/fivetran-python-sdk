from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class GetTeamMembershipInConnectorPathParams:
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'teamId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetTeamMembershipInConnectorHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetTeamMembershipInConnectorRequest:
    headers: GetTeamMembershipInConnectorHeaders = dataclasses.field()
    path_params: GetTeamMembershipInConnectorPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetTeamMembershipInConnectorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_team_membership_in_connector_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    