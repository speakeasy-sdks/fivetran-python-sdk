"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fivetran import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrustCertificateRequest:
    
    encoded_cert: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encoded_cert') }})
    r"""The certificate encoded in base64."""  
    hash: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hash') }})
    r"""Hash of the certificate."""  
    connector_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connector_id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for the connector"""  
    destination_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination_id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for the destination."""  
    