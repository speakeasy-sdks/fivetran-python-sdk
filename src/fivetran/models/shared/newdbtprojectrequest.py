"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewDbtProjectRequest:
    
    dbt_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt_version'), 'exclude': lambda f: f is None }})

    r"""The version of dbt that should run the project."""
    default_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_schema'), 'exclude': lambda f: f is None }})

    r"""Default schema in destination."""
    folder_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('folder_path'), 'exclude': lambda f: f is None }})

    r"""Folder in Git repo."""
    git_branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('git_branch'), 'exclude': lambda f: f is None }})

    r"""Git branch."""
    git_remote_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('git_remote_url'), 'exclude': lambda f: f is None }})

    r"""Git remote url."""
    group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_id'), 'exclude': lambda f: f is None }})

    r"""The unique identifier for the Group within the Fivetran system."""
    target_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_name'), 'exclude': lambda f: f is None }})

    r"""Target name to set or override the value from the deployment.yaml."""
    threads: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('threads'), 'exclude': lambda f: f is None }})

    r"""The number of threads dbt will use."""
    