# AppResourceTypeServiceGetResponse

The AppResourceTypeServiceGetResponse contains an expanded array containing the expanded values indicated by the expand mask
 in the request and an app resource type view containing the resource type and JSONPATHs indicating which objects are where in the expand mask.


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `app_resource_type_view`                                                    | [Optional[AppResourceTypeView]](../../models/shared/appresourcetypeview.md) | :heavy_minus_sign:                                                          | The AppResourceTypeView message.                                            |
| `expanded`                                                                  | list[dict[str, *Any*]]                                                      | :heavy_minus_sign:                                                          | List of serialized related objects.                                         |