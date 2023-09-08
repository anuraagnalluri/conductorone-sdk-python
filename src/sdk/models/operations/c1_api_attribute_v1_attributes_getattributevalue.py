"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getattributevalueresponse as shared_getattributevalueresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAttributeV1AttributesGetAttributeValueRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class C1APIAttributeV1AttributesGetAttributeValueResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_attribute_value_response: Optional[shared_getattributevalueresponse.GetAttributeValueResponse] = dataclasses.field(default=None)
    r"""GetAttributeValueResponse is the response for getting an attribute value by id."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
