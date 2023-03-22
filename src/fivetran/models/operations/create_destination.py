"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import newdestinationrequest as shared_newdestinationrequest
from typing import Any, Optional


@dataclasses.dataclass
class CreateDestinationRequest:
    
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    new_destination_request: Optional[shared_newdestinationrequest.NewDestinationRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class CreateDestinationResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    create_destination_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    