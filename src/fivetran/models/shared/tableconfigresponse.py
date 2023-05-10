"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import columnconfigresponse as shared_columnconfigresponse
from ..shared import tableenabledpatchsettings as shared_tableenabledpatchsettings
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from fivetran import utils
from typing import Optional

class TableConfigResponseSyncModeEnum(str, Enum):
    r"""This field appears in the response if the connector supports switching sync modes for tables"""
    SOFT_DELETE = 'SOFT_DELETE'
    HISTORY = 'HISTORY'
    LIVE = 'LIVE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TableConfigResponse:
    
    columns: Optional[dict[str, shared_columnconfigresponse.ColumnConfigResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('columns'), 'exclude': lambda f: f is None }})
    r"""The set of columns within your table schema config that are synced into the destination"""
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""The boolean value specifying whether the sync for the table into the destination is enabled."""
    enabled_patch_settings: Optional[shared_tableenabledpatchsettings.TableEnabledPatchSettings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled_patch_settings'), 'exclude': lambda f: f is None }})
    name_in_destination: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name_in_destination'), 'exclude': lambda f: f is None }})
    r"""The schema name within your destination in accordance with Fivetran conventional rules"""
    sync_mode: Optional[TableConfigResponseSyncModeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync_mode'), 'exclude': lambda f: f is None }})
    r"""This field appears in the response if the connector supports switching sync modes for tables"""
    