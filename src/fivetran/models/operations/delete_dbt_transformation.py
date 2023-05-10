"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclasses.dataclass
class DeleteDbtTransformationRequest:
    
    transformation_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transformationId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the DBT Transformation within the Fivetran system."""
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteDbtTransformation200ApplicationJSON:
    r"""Successful response"""
    
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""Response status code"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""Response status text"""
    

@dataclasses.dataclass
class DeleteDbtTransformationResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_dbt_transformation_200_application_json_object: Optional[DeleteDbtTransformation200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    