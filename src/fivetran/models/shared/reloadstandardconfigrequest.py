"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReloadStandardConfigRequest:
    
    exclude_mode: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exclude_mode'), 'exclude': lambda f: f is None }})
    r"""Specifies whether all schemas and tables will be enabled or disabled in the standard config"""
    