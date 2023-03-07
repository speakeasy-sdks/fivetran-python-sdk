from __future__ import annotations
import dataclasses
from ..shared import connectcardconfig as shared_connectcardconfig
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewConnectorRequestV1:
    connect_card_config: Optional[shared_connectcardconfig.ConnectCardConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connect_card_config'), 'exclude': lambda f: f is None }})
    daily_sync_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('daily_sync_time'), 'exclude': lambda f: f is None }})
    group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_id'), 'exclude': lambda f: f is None }})
    pause_after_trial: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pause_after_trial'), 'exclude': lambda f: f is None }})
    paused: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paused'), 'exclude': lambda f: f is None }})
    run_setup_tests: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('run_setup_tests'), 'exclude': lambda f: f is None }})
    schedule_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule_type'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})
    sync_frequency: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync_frequency'), 'exclude': lambda f: f is None }})
    trust_certificates: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trust_certificates'), 'exclude': lambda f: f is None }})
    trust_fingerprints: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trust_fingerprints'), 'exclude': lambda f: f is None }})
    