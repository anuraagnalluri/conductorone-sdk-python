"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import appentitlementref as shared_appentitlementref
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RequestCatalogManagementServiceAddAppEntitlementsRequest:
    r"""The RequestCatalogManagementServiceAddAppEntitlementsRequest object is used to add app requestable app entitlements to a request catalog."""
    app_entitlements: Optional[list[shared_appentitlementref.AppEntitlementRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlements'), 'exclude': lambda f: f is None }})
    r"""List of entitlements to add to the request catalog."""
    

