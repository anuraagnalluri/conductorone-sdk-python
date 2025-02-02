"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import requestcatalogmanagementservicelistentitlementspercatalogresponse as shared_requestcatalogmanagementservicelistentitlementspercatalogresponse
from typing import Optional



@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsPerCatalogRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalog_id', 'style': 'simple', 'explode': False }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsPerCatalogResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    request_catalog_management_service_list_entitlements_per_catalog_response: Optional[shared_requestcatalogmanagementservicelistentitlementspercatalogresponse.RequestCatalogManagementServiceListEntitlementsPerCatalogResponse] = dataclasses.field(default=None)
    r"""The RequestCatalogManagementServiceListEntitlementsPerCatalogResponse message contains a list of results and a nextPageToken if applicable."""
    

