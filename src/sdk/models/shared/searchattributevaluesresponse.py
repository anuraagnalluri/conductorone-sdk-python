"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import attributevalue as shared_attributevalue
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SearchAttributeValuesResponse:
    r"""SearchAttributeValuesResponse is the response for searching AttributeValues."""
    list_: Optional[list[shared_attributevalue.AttributeValue]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list'), 'exclude': lambda f: f is None }})
    r"""The list of returned AttributeValues."""
    next_page_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nextPageToken'), 'exclude': lambda f: f is None }})
    r"""The nextPageToken is shown for the next page if the number of results is larger than the max page size.
     The server returns one page of results and the nextPageToken until all results are retreived.
     To retrieve the next page, use the same request and append a pageToken field with the value of nextPageToken shown on the previous page.
    """
    

