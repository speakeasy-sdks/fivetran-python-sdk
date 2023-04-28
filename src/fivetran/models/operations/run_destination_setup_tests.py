"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import destinationresponse as shared_destinationresponse
from ..shared import runsetuptestsrequest as shared_runsetuptestsrequest
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclasses.dataclass
class RunDestinationSetupTestsRequest:
    
    destination_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'destinationId', 'style': 'simple', 'explode': False }})

    r"""The unique identifier for the destination within your Fivetran account."""
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})

    run_setup_tests_request: Optional[shared_runsetuptestsrequest.RunSetupTestsRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RunDestinationSetupTests200ApplicationJSON:
    r"""Successful response"""
    
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})

    r"""Response status code"""
    data: Optional[shared_destinationresponse.DestinationResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})

    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})

    r"""Response status text"""
    

@dataclasses.dataclass
class RunDestinationSetupTestsResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    run_destination_setup_tests_200_application_json_object: Optional[RunDestinationSetupTests200ApplicationJSON] = dataclasses.field(default=None)

    r"""Successful response"""
    