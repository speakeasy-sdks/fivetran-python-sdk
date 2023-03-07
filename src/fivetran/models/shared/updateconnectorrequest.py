from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from fivetran import utils
from typing import Any, Optional

class UpdateConnectorRequestScheduleTypeEnum(str, Enum):
    AUTO = "auto"
    MANUAL = "manual"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateConnectorRequest:
    auth: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth'), 'exclude': lambda f: f is None }})
    config: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('config'), 'exclude': lambda f: f is None }})
    daily_sync_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('daily_sync_time'), 'exclude': lambda f: f is None }})
    is_historical_sync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_historical_sync'), 'exclude': lambda f: f is None }})
    pause_after_trial: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pause_after_trial'), 'exclude': lambda f: f is None }})
    paused: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paused'), 'exclude': lambda f: f is None }})
    paused_after_trial: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paused_after_trial'), 'exclude': lambda f: f is None }})
    run_setup_tests: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('run_setup_tests'), 'exclude': lambda f: f is None }})
    schedule_type: Optional[UpdateConnectorRequestScheduleTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule_type'), 'exclude': lambda f: f is None }})
    schema_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema_status'), 'exclude': lambda f: f is None }})
    sync_frequency: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync_frequency'), 'exclude': lambda f: f is None }})
    trust_certificates: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trust_certificates'), 'exclude': lambda f: f is None }})
    trust_fingerprints: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trust_fingerprints'), 'exclude': lambda f: f is None }})
    