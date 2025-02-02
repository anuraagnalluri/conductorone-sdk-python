"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import taskexpandmask as shared_taskexpandmask
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskActionsServiceApproveRequest:
    r"""The TaskActionsServiceApproveRequest object lets you approve a task."""
    policy_step_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyStepId') }})
    r"""The ID of the policy step on the given task to approve."""
    comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment'), 'exclude': lambda f: f is None }})
    r"""The comment attached to the request."""
    task_expand_mask: Optional[shared_taskexpandmask.TaskExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The task expand mask is an array of strings that specifes the related objects the requester wishes to have returned when making a request where the expand mask is part of the input. Use '*' to view all possible responses."""
    

