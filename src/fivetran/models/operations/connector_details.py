"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ConnectorDetailsRequest:
    
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the connector within the Fivetran system"""  
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class ConnectorDetailsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    connector_details_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    