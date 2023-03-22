"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ListAllRolesRequest:
    
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Paging cursor, [read more about pagination](https://fivetran.com/docs/rest-api/pagination)"""  
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Number of records to fetch per page. Accepts a number in the range 1..1000; the default value is 100."""  
    

@dataclasses.dataclass
class ListAllRolesResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    list_all_roles_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    