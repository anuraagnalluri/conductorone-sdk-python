"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getrolesresponse as shared_getrolesresponse
from typing import Optional



@dataclasses.dataclass
class C1APIIamV1RolesGetRequest:
    role_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'role_id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class C1APIIamV1RolesGetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_roles_response: Optional[shared_getrolesresponse.GetRolesResponse] = dataclasses.field(default=None)
    r"""The GetRolesResponse message contains the retrieved role."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

