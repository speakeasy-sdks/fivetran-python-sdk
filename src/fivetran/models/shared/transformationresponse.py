"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import transformationschedule as shared_transformationschedule
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from fivetran import utils
from marshmallow import fields
from typing import Optional

class TransformationResponseStatusEnum(str, Enum):
    r"""The status of DBT Transformation."""
    SUCCEEDED = 'SUCCEEDED'
    RUNNING = 'RUNNING'
    FAILED = 'FAILED'
    PENDING = 'PENDING'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransformationResponse:
    
    dbt_model_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt_model_id'), 'exclude': lambda f: f is None }})

    r"""The unique identifier for the DBT Model within the Fivetran system."""
    dbt_project_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt_project_id'), 'exclude': lambda f: f is None }})

    r"""The unique identifier for the DBT Project within the Fivetran system."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})

    r"""The unique identifier for the DBT Model within the Fivetran system."""
    last_run: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_run'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})

    r"""The timestamp of last DBT Transformation run."""
    next_run: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_run'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})

    r"""The timestamp of next DBT Transformation run."""
    output_model_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('output_model_name'), 'exclude': lambda f: f is None }})

    r"""The DBT Model name."""
    run_tests: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('run_tests'), 'exclude': lambda f: f is None }})

    r"""The field indicates whether the tests has been confugured for DBT Transformation."""
    schedule: Optional[shared_transformationschedule.TransformationSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})

    status: Optional[TransformationResponseStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})

    r"""The status of DBT Transformation."""
    