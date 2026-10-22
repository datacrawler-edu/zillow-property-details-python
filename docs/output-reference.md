# Output reference

Records may represent a property, building or community; recordType identifies the shape. Fields can be unavailable or null.

| Field | Meaning |
|---|---|
| `recordType` | Record type |
| `recordId` | Record identity |
| `sourceInput` | Input reference |
| `zpid` | ZPID |
| `lotId` | Building lot ID |
| `propertyUrl` | Property URL |
| `listingAddress` | Address |
| `listingPrice` | Listing price |
| `listingStatus` | Listing status |
| `homeType` | Home type |
| `bedrooms` | Bedrooms |
| `bathrooms` | Bathrooms |
| `livingArea` | Living area |
| `yearBuilt` | Year built |
| `description` | Description |
| `photos` | Photos |
| `priceHistory` | Price history |
| `taxHistory` | Tax history |
| `schools` | Schools |
| `agent` | Listing agent |
| `contactAgent` | Displayed contact agent |
| `buildingName` | Building name |
| `floorPlans` | Floor plans |
| `units` | Building units |
| `scrapedAt` | Captured at |
| `plid` | Community PLID |
| `propertyCount` | Available inventory count |
| `properties` | Available property IDs |

The [sample](../data/sample-output.json) is a small projection of a real successful Dataset record, observed 2026-10-22. It is not a complete record or current market valuation. Contact fields and narrative were omitted. Photos are URLs. A completed run does not guarantee every requested property or unit was available. Inspect the run and SUMMARY record as well as Dataset rows.
