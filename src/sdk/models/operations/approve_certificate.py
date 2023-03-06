from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import trustcertificaterequest as shared_trustcertificaterequest
from typing import Any, Optional


@dataclasses.dataclass
class ApproveCertificateHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ApproveCertificateRequest:
    headers: ApproveCertificateHeaders = dataclasses.field()
    request: Optional[shared_trustcertificaterequest.TrustCertificateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ApproveCertificateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    approve_certificate_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    