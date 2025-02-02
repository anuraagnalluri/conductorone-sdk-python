"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import appentitlement as shared_appentitlement
from ..shared import appentitlementexpandmask as shared_appentitlementexpandmask
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateAppEntitlementRequestInput:
    r"""The UpdateAppEntitlementRequest message contains the app entitlement and the fields to be updated."""
    app_entitlement: Optional[shared_appentitlement.AppEntitlementInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entitlement'), 'exclude': lambda f: f is None }})
    r"""The app entitlement represents one permission in a downstream App (SAAS) that can be granted. For example, GitHub Read vs GitHub Write.

    This message contains a oneof named max_grant_duration. Only a single field of the following list may be set at a time:
      - durationUnset
      - durationGrant
    """
    app_entitlement_expand_mask: Optional[shared_appentitlementexpandmask.AppEntitlementExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The app entitlement expand mask allows the user to get additional information when getting responses containing app entitlement views."""
    update_mask: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updateMask'), 'exclude': lambda f: f is None }})
    

