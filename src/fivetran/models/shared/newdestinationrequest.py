from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from fivetran import utils
from typing import Optional

class NewDestinationRequestRegionEnum(str, Enum):
    GCP_US_EAST4 = "GCP_US_EAST4"
    GCP_US_WEST1 = "GCP_US_WEST1"
    GCP_EUROPE_WEST3 = "GCP_EUROPE_WEST3"
    GCP_AUSTRALIA_SOUTHEAST1 = "GCP_AUSTRALIA_SOUTHEAST1"
    GCP_NORTHAMERICA_NORTHEAST1 = "GCP_NORTHAMERICA_NORTHEAST1"
    GCP_EUROPE_WEST2 = "GCP_EUROPE_WEST2"
    GCP_ASIA_SOUTHEAST1 = "GCP_ASIA_SOUTHEAST1"
    AWS_US_EAST_1 = "AWS_US_EAST_1"
    AWS_US_EAST_2 = "AWS_US_EAST_2"
    AWS_US_WEST_2 = "AWS_US_WEST_2"
    AWS_AP_SOUTHEAST_2 = "AWS_AP_SOUTHEAST_2"
    AWS_EU_CENTRAL_1 = "AWS_EU_CENTRAL_1"
    AWS_EU_WEST_1 = "AWS_EU_WEST_1"
    AWS_EU_WEST_2 = " AWS_EU_WEST_2"
    AZURE_EASTUS2 = "AZURE_EASTUS2"
    AZURE_AUSTRALIAEAST = "AZURE_AUSTRALIAEAST"
    GCP_ASIA_SOUTH1 = "GCP_ASIA_SOUTH1"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewDestinationRequest:
    group_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_id') }})
    service: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service') }})
    time_zone_offset: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time_zone_offset') }})
    region: Optional[NewDestinationRequestRegionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    run_setup_tests: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('run_setup_tests'), 'exclude': lambda f: f is None }})
    trust_certificates: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trust_certificates'), 'exclude': lambda f: f is None }})
    trust_fingerprints: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trust_fingerprints'), 'exclude': lambda f: f is None }})
    