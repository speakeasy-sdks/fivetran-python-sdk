"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import runsetuptestsrequest as shared_runsetuptestsrequest
from typing import Any, Optional


@dataclasses.dataclass
class RunSetupTestsRequest:
    
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the connector within the Fivetran system"""  
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    run_setup_tests_request: Optional[shared_runsetuptestsrequest.RunSetupTestsRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class RunSetupTestsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    run_setup_tests_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful response"""  
    