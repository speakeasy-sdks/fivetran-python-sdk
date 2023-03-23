"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import transformationschedule as shared_transformationschedule
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewTransformationRequest:
    
    dbt_model_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt_model_id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for the DBT Model within the Fivetran system."""  
    run_tests: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('run_tests'), 'exclude': lambda f: f is None }})
    r"""The field indicates whether the tests has been confugured for DBT Transformation."""  
    schedule: Optional[shared_transformationschedule.TransformationSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})  
    