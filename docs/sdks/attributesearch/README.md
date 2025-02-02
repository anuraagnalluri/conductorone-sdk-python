# attribute_search

### Available Operations

* [search_attribute_values](#search_attribute_values) - Search Attribute Values

## search_attribute_values

Search attributes based on filters specified in the request body.

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

req = shared.SearchAttributeValuesRequest(
    attribute_type_ids=[
        'recusandae',
    ],
    exclude_ids=[
        'omnis',
    ],
    ids=[
        'facilis',
    ],
    page_size=5966.56,
    page_token='voluptatem',
    query='porro',
    value='consequuntur',
)

res = s.attribute_search.search_attribute_values(req)

if res.search_attribute_values_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.SearchAttributeValuesRequest](../../models/shared/searchattributevaluesrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.C1APIAttributeV1AttributeSearchSearchAttributeValuesResponse](../../models/operations/c1apiattributev1attributesearchsearchattributevaluesresponse.md)**

