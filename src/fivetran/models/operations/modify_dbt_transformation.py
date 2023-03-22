"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import updatetransformationrequest as shared_updatetransformationrequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyDbtTransformationRequest:
    
    transformation_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transformationId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the DBT Transformation within the Fivetran system."""  
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    update_transformation_request: Optional[shared_updatetransformationrequest.UpdateTransformationRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class ModifyDbtTransformationResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    modify_dbt_transformation_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    