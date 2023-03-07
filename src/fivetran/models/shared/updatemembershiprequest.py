from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateMembershipRequest:
    role: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    