"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectorservicecreaterequest as shared_connectorservicecreaterequest
from ..shared import connectorservicecreateresponse as shared_connectorservicecreateresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1ConnectorServiceCreateRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    connector_service_create_request: Optional[shared_connectorservicecreaterequest.ConnectorServiceCreateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class C1APIAppV1ConnectorServiceCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connector_service_create_response: Optional[shared_connectorservicecreateresponse.ConnectorServiceCreateResponse] = dataclasses.field(default=None)
    r"""The ConnectorServiceCreateResponse is the response returned from creating a connector."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

