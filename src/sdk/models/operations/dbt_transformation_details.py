from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DbtTransformationDetailsPathParams:
    transformation_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transformationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DbtTransformationDetailsHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DbtTransformationDetailsRequest:
    headers: DbtTransformationDetailsHeaders = dataclasses.field()
    path_params: DbtTransformationDetailsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DbtTransformationDetailsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    dbt_transformation_details_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    