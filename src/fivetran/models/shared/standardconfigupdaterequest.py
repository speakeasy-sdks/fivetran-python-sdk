from __future__ import annotations
import dataclasses
from ..shared import schemaupdaterequest as shared_schemaupdaterequest
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from fivetran import utils
from typing import Optional

class StandardConfigUpdateRequestSchemaChangeHandlingEnum(str, Enum):
    ALLOW_ALL = "ALLOW_ALL"
    ALLOW_COLUMNS = "ALLOW_COLUMNS"
    BLOCK_ALL = "BLOCK_ALL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StandardConfigUpdateRequest:
    schema_change_handling: Optional[StandardConfigUpdateRequestSchemaChangeHandlingEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema_change_handling'), 'exclude': lambda f: f is None }})
    schemas: Optional[dict[str, shared_schemaupdaterequest.SchemaUpdateRequest]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemas'), 'exclude': lambda f: f is None }})
    