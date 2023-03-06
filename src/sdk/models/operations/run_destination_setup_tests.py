from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import runsetuptestsrequest as shared_runsetuptestsrequest
from typing import Any, Optional


@dataclasses.dataclass
class RunDestinationSetupTestsPathParams:
    destination_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'destinationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RunDestinationSetupTestsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RunDestinationSetupTestsRequest:
    headers: RunDestinationSetupTestsHeaders = dataclasses.field()
    path_params: RunDestinationSetupTestsPathParams = dataclasses.field()
    request: Optional[shared_runsetuptestsrequest.RunSetupTestsRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class RunDestinationSetupTestsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    run_destination_setup_tests_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    