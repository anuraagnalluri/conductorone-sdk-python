"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import appuser as shared_appuser
from ..shared import appuserexpandmask as shared_appuserexpandmask
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AppUserServiceUpdateRequestInput:
    r"""The AppUserServiceUpdateRequest message contains the app user and the fields to be updated."""
    app_user: Optional[shared_appuser.AppUserInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUser'), 'exclude': lambda f: f is None }})
    r"""Application User that represents an account in the application."""
    app_user_expand_mask: Optional[shared_appuserexpandmask.AppUserExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The AppUserExpandMask message contains a list of paths to expand in the response."""
    update_mask: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updateMask'), 'exclude': lambda f: f is None }})
    

