# Input reference

| Field | Type | Behavior |
|---|---|---|
| `startUrls` | array | HTTPS Zillow home, building, apartment or community URLs. Individual properties need a ZPID; building identifiers are resolved automatically. Source availability can vary. |
| `addresses` | array | Full property addresses. Only one exact normalized address and unit match is accepted; ambiguous or unavailable addresses are reported in the summary. |
| `propertyStatus` | string | Compatibility hint. Actual source status determines the result; this hint does not override source data. |
| `extractBuildingUnits` | string | Disabled returns one building record with available unit and floor-plan information, or a community inventory record. Other selections collect details for matching units supplied by the source. Inventory is not guaranteed exhaustive. |
| `searchResultsDatasetId` | string | Optional Dataset ID. Reads up to 1000 rows containing a valid Zillow propertyUrl, url, detailUrl or positive ZPID. Duplicate properties are saved only once across the run. |
| `maxResults` | integer | Requested ceiling of unique property, unit, building or community records across the run, including records retained on restart. Source availability can produce fewer results. |

See [sample input](../data/sample-input.json). maxResults defaults to 100; the safe sample uses 1. Allowed range: 1–10,000. Dataset import reads up to 1,000 input rows. propertyStatus is a compatibility hint, not an instruction to change the actual listing status. There is no separate direct-ZPID input field.
