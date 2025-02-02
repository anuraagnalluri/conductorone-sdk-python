"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import policy as shared_policy
from ..shared import policystep as shared_policystep
from ..shared import policystepinstance as shared_policystepinstance
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PolicyInstance:
    r"""A policy instance is an object that contains a reference to the policy it was created from, the currently executing step, the next steps, and the history of previously completed steps."""
    history: Optional[list[shared_policystepinstance.PolicyStepInstance]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('history'), 'exclude': lambda f: f is None }})
    r"""An array of steps that were previously processed by the ticket with their outcomes set, in order."""
    next: Optional[list[shared_policystep.PolicyStep]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})
    r"""An array of steps that will be processed by the ticket, in order."""
    policy: Optional[shared_policy.Policy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policy'), 'exclude': lambda f: f is None }})
    r"""A policy describes the behavior of the ConductorOne system when processing a task. You can describe the type, approvers, fallback behavior, and escalation processes."""
    policy_step_instance: Optional[shared_policystepinstance.PolicyStepInstance] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current'), 'exclude': lambda f: f is None }})
    r"""The policy step instance includes a reference to an instance of a policy step that tracks state and has a unique ID.

    This message contains a oneof named instance. Only a single field of the following list may be set at a time:
      - approval
      - provision
    """
    

