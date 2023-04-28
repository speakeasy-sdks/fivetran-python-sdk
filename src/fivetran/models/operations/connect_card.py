"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectcardconfigrequest as shared_connectcardconfigrequest
from ..shared import connectorconnectcardresponse as shared_connectorconnectcardresponse
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclasses.dataclass
class ConnectCardRequest:
    
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectorId', 'style': 'simple', 'explode': False }})

    r"""The unique identifier for the connector within the Fivetran system"""
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})

    connect_card_config_request: Optional[shared_connectcardconfigrequest.ConnectCardConfigRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectCard200ApplicationJSON:
    r"""Successful response"""
    
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})

    r"""Response status code"""
    data: Optional[shared_connectorconnectcardresponse.ConnectorConnectCardResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})

    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})

    r"""Response status text"""
    

@dataclasses.dataclass
class ConnectCardResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    connect_card_200_application_json_object: Optional[ConnectCard200ApplicationJSON] = dataclasses.field(default=None)

    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    