# app_entitlement_owners

### Available Operations

* [add](#add) - Add
* [list](#list) - List
* [remove](#remove) - Remove
* [set](#set) - Set

## add

Add an owner to a given app entitlement.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementOwnersAddRequest(
    add_app_entitlement_owner_request=shared.AddAppEntitlementOwnerRequest(
        user_id='quibusdam',
    ),
    app_id='unde',
    entitlement_id='nulla',
)

res = s.app_entitlement_owners.add(req)

if res.add_app_entitlement_owner_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APIAppV1AppEntitlementOwnersAddRequest](../../models/operations/c1apiappv1appentitlementownersaddrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.C1APIAppV1AppEntitlementOwnersAddResponse](../../models/operations/c1apiappv1appentitlementownersaddresponse.md)**


## list

List owners for a given app entitlement.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementOwnersListRequest(
    app_id='corrupti',
    entitlement_id='illum',
    page_size=4236.55,
    page_token='error',
)

res = s.app_entitlement_owners.list(req)

if res.list_app_entitlement_owners_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIAppV1AppEntitlementOwnersListRequest](../../models/operations/c1apiappv1appentitlementownerslistrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.C1APIAppV1AppEntitlementOwnersListResponse](../../models/operations/c1apiappv1appentitlementownerslistresponse.md)**


## remove

Remove an owner from a given app entitlement.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementOwnersRemoveRequest(
    remove_app_entitlement_owner_request=shared.RemoveAppEntitlementOwnerRequest(),
    app_id='deserunt',
    entitlement_id='suscipit',
    user_id='iure',
)

res = s.app_entitlement_owners.remove(req)

if res.remove_app_entitlement_owner_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIAppV1AppEntitlementOwnersRemoveRequest](../../models/operations/c1apiappv1appentitlementownersremoverequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APIAppV1AppEntitlementOwnersRemoveResponse](../../models/operations/c1apiappv1appentitlementownersremoveresponse.md)**


## set

Sets the owners for a given app entitlement to the specified list of users.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIAppV1AppEntitlementOwnersSetRequest(
    set_app_entitlement_owners_request=shared.SetAppEntitlementOwnersRequest(
        user_ids=[
            'magnam',
        ],
    ),
    app_id='debitis',
    entitlement_id='ipsa',
)

res = s.app_entitlement_owners.set(req)

if res.set_app_entitlement_owners_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APIAppV1AppEntitlementOwnersSetRequest](../../models/operations/c1apiappv1appentitlementownerssetrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.C1APIAppV1AppEntitlementOwnersSetResponse](../../models/operations/c1apiappv1appentitlementownerssetresponse.md)**

