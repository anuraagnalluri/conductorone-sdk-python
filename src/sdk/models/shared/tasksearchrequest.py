"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import taskexpandmask as shared_taskexpandmask
from ..shared import taskref as shared_taskref
from ..shared import tasktype as shared_tasktype
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from sdk import utils
from typing import Optional

class TaskSearchRequestCurrentStep(str, Enum):
    r"""Search tasks that have this type of step as the current step."""
    TASK_SEARCH_CURRENT_STEP_UNSPECIFIED = 'TASK_SEARCH_CURRENT_STEP_UNSPECIFIED'
    TASK_SEARCH_CURRENT_STEP_APPROVAL = 'TASK_SEARCH_CURRENT_STEP_APPROVAL'
    TASK_SEARCH_CURRENT_STEP_PROVISION = 'TASK_SEARCH_CURRENT_STEP_PROVISION'

class TaskSearchRequestEmergencyStatus(str, Enum):
    r"""Search tasks that are or are not emergency access."""
    UNSPECIFIED = 'UNSPECIFIED'
    ALL = 'ALL'
    NON_EMERGENCY = 'NON_EMERGENCY'
    EMERGENCY = 'EMERGENCY'

class TaskSearchRequestSortBy(str, Enum):
    r"""Sort tasks in a specific order."""
    TASK_SEARCH_SORT_BY_UNSPECIFIED = 'TASK_SEARCH_SORT_BY_UNSPECIFIED'
    TASK_SEARCH_SORT_BY_ACCOUNT = 'TASK_SEARCH_SORT_BY_ACCOUNT'
    TASK_SEARCH_SORT_BY_RESOURCE = 'TASK_SEARCH_SORT_BY_RESOURCE'
    TASK_SEARCH_SORT_BY_ACCOUNT_OWNER = 'TASK_SEARCH_SORT_BY_ACCOUNT_OWNER'
    TASK_SEARCH_SORT_BY_REVERSE_TICKET_ID = 'TASK_SEARCH_SORT_BY_REVERSE_TICKET_ID'

class TaskSearchRequestTaskStates(str, Enum):
    TASK_STATE_UNSPECIFIED = 'TASK_STATE_UNSPECIFIED'
    TASK_STATE_OPEN = 'TASK_STATE_OPEN'
    TASK_STATE_CLOSED = 'TASK_STATE_CLOSED'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskSearchRequestInput:
    r"""Search for tasks based on a plethora filters."""
    access_review_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accessReviewIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks that belong to any of the access reviews included in this list."""
    account_owner_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountOwnerIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks that have any of these account owners."""
    actor_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actorId'), 'exclude': lambda f: f is None }})
    r"""Search tasks that have this actor ID."""
    app_entitlement_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlementIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks that have any of these app entitlement IDs."""
    application_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('applicationIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks that have any of these apps as targets."""
    app_resource_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appResourceIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks that have any of these app resource IDs."""
    app_resource_type_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appResourceTypeIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks that have any of these app resource type IDs."""
    app_user_subject_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUserSubjectIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks that have any of these app users as subjects."""
    assignees_in_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assigneesInIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks by  List of UserIDs which are currently assigned these Tasks"""
    created_after: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAfter'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    created_before: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdBefore'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    current_step: Optional[TaskSearchRequestCurrentStep] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentStep'), 'exclude': lambda f: f is None }})
    r"""Search tasks that have this type of step as the current step."""
    emergency_status: Optional[TaskSearchRequestEmergencyStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emergencyStatus'), 'exclude': lambda f: f is None }})
    r"""Search tasks that are or are not emergency access."""
    exclude_app_entitlement_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('excludeAppEntitlementIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks that do not have any of these app entitlement IDs."""
    exclude_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('excludeIds'), 'exclude': lambda f: f is None }})
    r"""Exclude Specific TaskIDs from this serach result."""
    include_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('includeDeleted'), 'exclude': lambda f: f is None }})
    r"""Whether or not to include deleted tasks."""
    my_work_user_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('myWorkUserIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks where the user would see this task in the My Work section"""
    opener_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openerIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks that were created by any of the users in this array."""
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize'), 'exclude': lambda f: f is None }})
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageToken'), 'exclude': lambda f: f is None }})
    r"""The pageToken field."""
    previously_acted_on_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previouslyActedOnIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks that were acted on by any of these users."""
    query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query'), 'exclude': lambda f: f is None }})
    r"""Fuzzy search tasks by display name or description. Also can search by numeric ID."""
    refs: Optional[list[shared_taskref.TaskRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refs'), 'exclude': lambda f: f is None }})
    r"""Query tasks by display name, description, or numeric ID."""
    sort_by: Optional[TaskSearchRequestSortBy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sortBy'), 'exclude': lambda f: f is None }})
    r"""Sort tasks in a specific order."""
    subject_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subjectIds'), 'exclude': lambda f: f is None }})
    r"""Search tasks where these users are the subject."""
    task_expand_mask: Optional[shared_taskexpandmask.TaskExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The task expand mask is an array of strings that specifes the related objects the requester wishes to have returned when making a request where the expand mask is part of the input. Use '*' to view all possible responses."""
    task_states: Optional[list[TaskSearchRequestTaskStates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taskStates'), 'exclude': lambda f: f is None }})
    r"""Search tasks with this task state."""
    task_types: Optional[list[shared_tasktype.TaskTypeInput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taskTypes'), 'exclude': lambda f: f is None }})
    r"""Search tasks with this task type. This is a oneOf, and needs an object, which can be empty, to sort."""
    

