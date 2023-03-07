from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import trustfingerprintrequest as shared_trustfingerprintrequest
from typing import Any, Optional


@dataclasses.dataclass
class ApproveFingerprintHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ApproveFingerprintRequest:
    headers: ApproveFingerprintHeaders = dataclasses.field()
    request: Optional[shared_trustfingerprintrequest.TrustFingerprintRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ApproveFingerprintResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    approve_fingerprint_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    