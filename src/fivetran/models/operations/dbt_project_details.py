"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import dbtprojectdetailsresponse as shared_dbtprojectdetailsresponse
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclasses.dataclass
class DbtProjectDetailsRequest:
    
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'projectId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the DBT Project within the Fivetran system."""
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DbtProjectDetails200ApplicationJSON:
    r"""Successful response"""
    
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    r"""Response status code"""
    data: Optional[shared_dbtprojectdetailsresponse.DbtProjectDetailsResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""Response status text"""
    

@dataclasses.dataclass
class DbtProjectDetailsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    dbt_project_details_200_application_json_object: Optional[DbtProjectDetails200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    