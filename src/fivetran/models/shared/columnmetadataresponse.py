"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ColumnMetadataResponse:
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique column identifier"""
    is_foreign_key: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_foreign_key'), 'exclude': lambda f: f is None }})
    r"""The boolean specifying whether the column is a foreign key"""
    is_primary_key: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_primary_key'), 'exclude': lambda f: f is None }})
    r"""The boolean specifying whether the column is a primary key"""
    name_in_destination: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name_in_destination'), 'exclude': lambda f: f is None }})
    r"""The column name in the destination"""
    name_in_source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name_in_source'), 'exclude': lambda f: f is None }})
    r"""The column name in the source"""
    parent_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parent_id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier of the table associated with the column"""
    type_in_destination: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type_in_destination'), 'exclude': lambda f: f is None }})
    r"""The column type in the destination"""
    type_in_source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type_in_source'), 'exclude': lambda f: f is None }})
    r"""The column type in the source"""
    