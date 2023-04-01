"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import resyncconnectorrequest as shared_resyncconnectorrequest
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclasses.dataclass
class ResyncConnectorRequest:
    
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the connector within the Fivetran system"""  
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    resync_connector_request: Optional[shared_resyncconnectorrequest.ResyncConnectorRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ResyncConnector200ApplicationJSON:
    r"""Successful response"""
    
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""Response status code"""  
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""Response status text"""  
    

@dataclasses.dataclass
class ResyncConnectorResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    resync_connector_200_application_json_object: Optional[ResyncConnector200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successful response"""  
    