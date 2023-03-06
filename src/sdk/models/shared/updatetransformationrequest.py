from __future__ import annotations
import dataclasses
from ..shared import transformationschedule as shared_transformationschedule
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateTransformationRequest:
    run_tests: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('run_tests'), 'exclude': lambda f: f is None }})
    schedule: Optional[shared_transformationschedule.TransformationSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})
    