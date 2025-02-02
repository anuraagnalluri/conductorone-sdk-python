"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import personalclientservicecreateresponse as shared_personalclientservicecreateresponse
from typing import Optional



@dataclasses.dataclass
class C1APIIamV1PersonalClientServiceCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    personal_client_service_create_response: Optional[shared_personalclientservicecreateresponse.PersonalClientServiceCreateResponse] = dataclasses.field(default=None)
    r"""The PersonalClientServiceCreateResponse message contains the created personal client and client secret."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

