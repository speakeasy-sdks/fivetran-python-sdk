"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ListAllConnectorsInGroupRequest:
    
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for the group within the Fivetran system."""  
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})  
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Paging cursor, [read more about pagination](https://fivetran.com/docs/rest-api/pagination)"""  
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Number of records to fetch per page. Accepts a number in the range 1..1000; the default value is 100."""  
    schema: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'schema', 'style': 'form', 'explode': True }})
    r"""The name used both as the connector's name within the Fivetran system and as the source schema's name within your destination."""  
    

@dataclasses.dataclass
class ListAllConnectorsInGroupResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    list_all_connectors_in_group_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    