from __future__ import annotations
import dataclasses
from ..shared import connectcardconfig as shared_connectcardconfig
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectCardConfigRequest:
    connect_card_config: Optional[shared_connectcardconfig.ConnectCardConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connect_card_config'), 'exclude': lambda f: f is None }})
    