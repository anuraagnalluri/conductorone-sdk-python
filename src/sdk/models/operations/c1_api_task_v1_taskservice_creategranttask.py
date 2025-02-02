"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import taskservicecreategrantresponse as shared_taskservicecreategrantresponse
from typing import Optional



@dataclasses.dataclass
class C1APITaskV1TaskServiceCreateGrantTaskResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    task_service_create_grant_response: Optional[shared_taskservicecreategrantresponse.TaskServiceCreateGrantResponse] = dataclasses.field(default=None)
    r"""The TaskServiceCreateGrantResponse returns a task view which has a task including JSONPATHs to the expanded items in the expanded array."""
    

