"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import appresourceservicelistresponse as shared_appresourceservicelistresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1AppResourceServiceListRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    app_resource_type_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_resource_type_id', 'style': 'simple', 'explode': False }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class C1APIAppV1AppResourceServiceListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    app_resource_service_list_response: Optional[shared_appresourceservicelistresponse.AppResourceServiceListResponse] = dataclasses.field(default=None)
    r"""The AppResourceServiceListResponse message contains a list of results and a nextPageToken if applicable."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

