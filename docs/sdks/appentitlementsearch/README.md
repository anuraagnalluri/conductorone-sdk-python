# app_entitlement_search

### Available Operations

* [search](#search) - Search

## search

Search app entitlements based on filters specified in the request body.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.AppEntitlementSearchServiceSearchRequest(
    app_entitlement_expand_mask=shared.AppEntitlementExpandMask(
        paths=[
            'delectus',
        ],
    ),
    access_review_id='tempora',
    alias='suscipit',
    app_ids=[
        'molestiae',
    ],
    app_user_ids=[
        'minus',
    ],
    compliance_framework_ids=[
        'placeat',
    ],
    exclude_app_ids=[
        'voluptatum',
    ],
    exclude_app_user_ids=[
        'iusto',
    ],
    only_get_expiring=False,
    page_size=5680.45,
    page_token='nisi',
    query='recusandae',
    resource_type_ids=[
        'temporibus',
    ],
    risk_level_ids=[
        'ab',
    ],
)

res = s.app_entitlement_search.search(req)

if res.app_entitlement_search_service_search_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [shared.AppEntitlementSearchServiceSearchRequest](../../models/shared/appentitlementsearchservicesearchrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.C1APIAppV1AppEntitlementSearchServiceSearchResponse](../../models/operations/c1apiappv1appentitlementsearchservicesearchresponse.md)**

