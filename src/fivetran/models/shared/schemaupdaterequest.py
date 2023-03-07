from __future__ import annotations
import dataclasses
from ..shared import tableupdaterequest as shared_tableupdaterequest
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SchemaUpdateRequest:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    tables: Optional[dict[str, shared_tableupdaterequest.TableUpdateRequest]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tables'), 'exclude': lambda f: f is None }})
    