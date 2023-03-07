from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DbtModelDetailsPathParams:
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'modelId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DbtModelDetailsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DbtModelDetailsRequest:
    headers: DbtModelDetailsHeaders = dataclasses.field()
    path_params: DbtModelDetailsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DbtModelDetailsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    dbt_model_details_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    