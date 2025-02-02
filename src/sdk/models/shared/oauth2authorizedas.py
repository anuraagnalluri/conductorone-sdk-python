"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Optional



@dataclasses.dataclass
class OAuth2AuthorizedAsInput:
    r"""OAuth2AuthorizedAs tracks the user that OAuthed with the connector."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OAuth2AuthorizedAs:
    r"""OAuth2AuthorizedAs tracks the user that OAuthed with the connector."""
    auth_email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authEmail'), 'exclude': lambda f: f is None }})
    r"""authEmail is the email of the user that authorized the connector using OAuth."""
    authorized_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorizedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

