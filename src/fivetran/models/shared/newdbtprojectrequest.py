from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewDbtProjectRequest:
    dbt_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt_version'), 'exclude': lambda f: f is None }})
    default_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_schema'), 'exclude': lambda f: f is None }})
    folder_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('folder_path'), 'exclude': lambda f: f is None }})
    git_branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('git_branch'), 'exclude': lambda f: f is None }})
    git_remote_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('git_remote_url'), 'exclude': lambda f: f is None }})
    group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_id'), 'exclude': lambda f: f is None }})
    target_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_name'), 'exclude': lambda f: f is None }})
    threads: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('threads'), 'exclude': lambda f: f is None }})
    