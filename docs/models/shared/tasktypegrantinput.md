# TaskTypeGrantInput

The TaskTypeGrant message indicates that a task is a grant task and all related details.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `task_grant_source`                                                                                  | [Optional[TaskGrantSource]](../../models/shared/taskgrantsource.md)                                  | :heavy_minus_sign:                                                                                   | The TaskGrantSource message tracks which external URL was the source of the specificed grant ticket. |