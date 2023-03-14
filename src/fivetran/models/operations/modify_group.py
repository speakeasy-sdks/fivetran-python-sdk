from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import updategrouprequest as shared_updategrouprequest
from typing import Any, Optional


@dataclasses.dataclass
class ModifyGroupRequest:
    group_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'groupId', 'style': 'simple', 'explode': False }})
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'Accept', 'style': 'simple', 'explode': False }})
    update_group_request: Optional[shared_updategrouprequest.UpdateGroupRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ModifyGroupResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    modify_group_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    