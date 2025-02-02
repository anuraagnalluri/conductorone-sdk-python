# AppResource

The app resource message is a single resource that can have entitlements.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `app_id`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The app that this resource belongs to.                               |
| `app_resource_type_id`                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The resource type that this resource is.                             |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `custom_description`                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | A custom description that can be set for a resource.                 |
| `deleted_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The description set for the resource.                                |
| `display_name`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The display name for this resource.                                  |
| `grant_count`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The number of grants to this resource.                               |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The id of the resource.                                              |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |