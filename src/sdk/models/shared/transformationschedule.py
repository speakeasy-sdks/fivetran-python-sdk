from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class TransformationScheduleDaysOfWeekEnum(str, Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

class TransformationScheduleScheduleTypeEnum(str, Enum):
    INTEGRATED = "INTEGRATED"
    TIME_OF_DAY = "TIME_OF_DAY"
    INTERVAL = "INTERVAL"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransformationSchedule:
    days_of_week: Optional[list[TransformationScheduleDaysOfWeekEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_of_week'), 'exclude': lambda f: f is None }})
    interval: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval'), 'exclude': lambda f: f is None }})
    schedule_type: Optional[TransformationScheduleScheduleTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule_type'), 'exclude': lambda f: f is None }})
    time_of_day: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time_of_day'), 'exclude': lambda f: f is None }})
    