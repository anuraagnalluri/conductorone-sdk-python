"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectorservicerevokecredentialrequest as shared_connectorservicerevokecredentialrequest
from ..shared import connectorservicerevokecredentialresponse as shared_connectorservicerevokecredentialresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1ConnectorServiceRevokeCredentialRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    connector_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connector_id', 'style': 'simple', 'explode': False }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    connector_service_revoke_credential_request: Optional[shared_connectorservicerevokecredentialrequest.ConnectorServiceRevokeCredentialRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class C1APIAppV1ConnectorServiceRevokeCredentialResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connector_service_revoke_credential_response: Optional[shared_connectorservicerevokecredentialresponse.ConnectorServiceRevokeCredentialResponse] = dataclasses.field(default=None)
    r"""Empty response body. Status code indicates success."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

