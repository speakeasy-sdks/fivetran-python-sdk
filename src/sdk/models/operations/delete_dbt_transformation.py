from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DeleteDbtTransformationPathParams:
    transformation_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transformationId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteDbtTransformationHeaders:
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteDbtTransformationRequest:
    headers: DeleteDbtTransformationHeaders = dataclasses.field()
    path_params: DeleteDbtTransformationPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteDbtTransformationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_dbt_transformation_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    