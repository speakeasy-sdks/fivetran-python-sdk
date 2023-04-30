"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import columnupdaterequest as shared_columnupdaterequest
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from fivetran import utils
from typing import Optional

class TableUpdateRequestSyncModeEnum(str, Enum):
    r"""This field appears in the response if the connector supports switching sync modes for tables"""
    SOFT_DELETE = 'SOFT_DELETE'
    HISTORY = 'HISTORY'
    LIVE = 'LIVE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TableUpdateRequest:
    
    columns: Optional[dict[str, shared_columnupdaterequest.ColumnUpdateRequest]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('columns'), 'exclude': lambda f: f is None }})
    r"""The set of columns within your table schema config that are synced into the destination"""
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""The boolean value specifying whether the sync for the table into the destination is enabled."""
    sync_mode: Optional[TableUpdateRequestSyncModeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync_mode'), 'exclude': lambda f: f is None }})
    r"""This field appears in the response if the connector supports switching sync modes for tables"""
    