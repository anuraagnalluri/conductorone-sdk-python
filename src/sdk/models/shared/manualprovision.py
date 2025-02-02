"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ManualProvision:
    r"""Manual provisioning indicates that a human must intervene for the provisioning of this step."""
    instructions: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instructions'), 'exclude': lambda f: f is None }})
    r"""This field indicates a text body of instructions for the provisioner to indicate."""
    user_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userIds'), 'exclude': lambda f: f is None }})
    r"""An array of users that are required to provision during this step."""
    

