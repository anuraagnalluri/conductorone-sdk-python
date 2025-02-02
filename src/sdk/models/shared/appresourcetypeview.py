"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import appresourcetype as shared_appresourcetype
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AppResourceTypeView:
    r"""The AppResourceTypeView message."""
    app_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appPath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the App object in the  array"""
    app_resource_type: Optional[shared_appresourcetype.AppResourceType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appResourceType'), 'exclude': lambda f: f is None }})
    r"""The AppResourceType is referenced by an app entitlement defining its resource types. Commonly things like Group or Role."""
    

