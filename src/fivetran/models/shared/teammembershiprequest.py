from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TeamMembershipRequest:
    role: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role'), 'exclude': lambda f: f is None }})
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id'), 'exclude': lambda f: f is None }})
    