"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import facetrangeitem as shared_facetrangeitem
from ..shared import facetvalueitem as shared_facetvalueitem
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FacetCategory:
    r"""The FacetCategory indicates a grouping of facets by type. For example, facets \\"OnePassword\\" and \\"Okta\\" would group under an \\"Apps\\" category.

    This message contains a oneof named item. Only a single field of the following list may be set at a time:
      - value
      - range
    """
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The display name of the category."""
    facet_range_item: Optional[shared_facetrangeitem.FacetRangeItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('range'), 'exclude': lambda f: f is None }})
    r"""The FacetRangeItem message."""
    facet_value_item: Optional[shared_facetvalueitem.FacetValueItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    r"""The FacetValueItem message."""
    icon_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iconUrl'), 'exclude': lambda f: f is None }})
    r"""An icon for the category."""
    param: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('param'), 'exclude': lambda f: f is None }})
    r"""The param that is being set when checking a facet in this category."""
    

