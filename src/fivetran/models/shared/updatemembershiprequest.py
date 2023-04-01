"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateMembershipRequest:
    
    role: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""The role that you would like to assign to the user"""  
    