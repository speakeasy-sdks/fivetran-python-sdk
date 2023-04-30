"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import setuptestresultresponse as shared_setuptestresultresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from fivetran import utils
from typing import Optional

class DestinationResponseRegionEnum(str, Enum):
    r"""Data processing location. This is where Fivetran will operate and run computation on data."""
    GCP_US_EAST4 = 'GCP_US_EAST4'
    GCP_US_WEST1 = 'GCP_US_WEST1'
    GCP_EUROPE_WEST3 = 'GCP_EUROPE_WEST3'
    GCP_AUSTRALIA_SOUTHEAST1 = 'GCP_AUSTRALIA_SOUTHEAST1'
    GCP_NORTHAMERICA_NORTHEAST1 = 'GCP_NORTHAMERICA_NORTHEAST1'
    GCP_EUROPE_WEST2 = 'GCP_EUROPE_WEST2'
    GCP_ASIA_SOUTHEAST1 = 'GCP_ASIA_SOUTHEAST1'
    AWS_US_EAST_1 = 'AWS_US_EAST_1'
    AWS_US_EAST_2 = 'AWS_US_EAST_2'
    AWS_US_WEST_2 = 'AWS_US_WEST_2'
    AWS_AP_SOUTHEAST_2 = 'AWS_AP_SOUTHEAST_2'
    AWS_EU_CENTRAL_1 = 'AWS_EU_CENTRAL_1'
    AWS_EU_WEST_1 = 'AWS_EU_WEST_1'
    AWS_EU_WEST_2 = ' AWS_EU_WEST_2'
    AZURE_EASTUS2 = 'AZURE_EASTUS2'
    AZURE_AUSTRALIAEAST = 'AZURE_AUSTRALIAEAST'
    GCP_ASIA_SOUTH1 = 'GCP_ASIA_SOUTH1'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationResponse:
    
    group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for the group within the Fivetran system."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for the destination within the Fivetran system"""
    region: Optional[DestinationResponseRegionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""Data processing location. This is where Fivetran will operate and run computation on data."""
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})
    r"""The name for the destination type within the Fivetran system."""
    setup_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('setup_status'), 'exclude': lambda f: f is None }})
    r"""Destination setup status"""
    setup_tests: Optional[list[shared_setuptestresultresponse.SetupTestResultResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('setup_tests'), 'exclude': lambda f: f is None }})
    r"""Setup tests results for this destination"""
    time_zone_offset: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time_zone_offset'), 'exclude': lambda f: f is None }})
    r"""Determines the time zone for the Fivetran sync schedule."""
    