# Zillow Property Details with Python

Turn known Zillow listing URLs, exact addresses or an existing Apify Dataset into available property facts and downloadable records. These examples call the [hosted Actor](https://apify.com/datascraperes/zillow-property-detail-scraper?fpr=edudata).

## What this repository helps you do

Collect property details for selected homes, enrich identifiers from a discovery workflow, and export existing results without collecting them again. Includes three Python workflows plus cURL and JavaScript requests. The repository contains integration examples; execution takes place on Apify.

## Example result

See the [JSON projection](data/sample-output.json) and [CSV projection](data/sample-output.csv) from a real successful record observed on 2026-10-22. Values are historical examples. Contacts and narrative were omitted; available fields vary.

## Run without code

Open the [Actor](https://apify.com/datascraperes/zillow-property-detail-scraper?fpr=edudata), keep the small example input, review pricing and limits, then Start. Inspect the run, SUMMARY and Dataset before exporting. Follow the [no-code guide](docs/no-code-guide.md).

## Try it with Apify's free plan

Apify currently offers $5 monthly prepaid usage and no credit card requirement on its free plan. Credits renew monthly and unused credits expire; Actor and platform charges consume available credit. Review the current [plan terms](https://apify.com/pricing?fpr=edudata). This is not a promise of unlimited free extraction. Links using fpr=edudata are affiliate links.

## Quick start for developers

Requires Python 3.10+; the Python examples use the standard library. Set APIFY_TOKEN in your environment without committing it. From the repository root:

```bash
python examples/python/property_details.py
```

The helper requests at most one record with a USD 0.02 Actor-charge limit and a 180-second server timeout. It saves the run ID before polling; a local wait timeout does not cancel the run. Inspect that ID before retrying.

## Input example

```json
{
  "startUrls": [
    {
      "url": "https://www.zillow.com/homedetails/17199-Park-Ave-Sonoma-CA-95476/15800416_zpid/"
    }
  ],
  "addresses": [],
  "propertyStatus": "FOR_SALE",
  "extractBuildingUnits": "disabled",
  "searchResultsDatasetId": "",
  "maxResults": 1
}
```

All six public inputs are documented in the [input reference](docs/input-reference.md). Addresses must match exactly; a status hint does not replace source status.

## Request examples

| Workflow | Example |
|---|---|
| One known listing | [Python property details](examples/python/property_details.py) |
| Existing search Dataset to details | [Python Dataset enrichment](examples/python/enrich_dataset.py) |
| Download existing results | [Python JSON/CSV export](examples/python/export_dataset.py) |
| Start through HTTP | [cURL](examples/curl-request.md) |
| Start with Node.js 20+ | [JavaScript](examples/javascript/request.mjs) |

The cURL and JavaScript examples start a run; their returned status is not evidence of completion. The Python helper saves available rows even when a terminal run fails. It never automatically repeats a billable start request.

## Output fields

Available data can include price, Zestimate, home facts, price/tax history, photo URLs, schools and contact information. recordType distinguishes property, building and community records. Fields can be null or unavailable. See [all output fields](docs/output-reference.md).

## Common use cases

- Enrich a shortlist of known homes with available facts and estimates.
- Read a discovery Dataset and add property-level records.
- Export collected records for spreadsheet review without a new Actor run.

## Enrich a Zillow search Dataset with Python

```bash
python examples/python/enrich_dataset.py YOUR_DATASET_ID
```

The source Dataset must be accessible to your account and contain supported URLs or positive ZPIDs. This example caps output at five records. The Actor reads at most 1,000 input rows; duplicate properties are saved once within the run. See [workflows](docs/use-cases.md).

## Export Zillow property records to CSV

```bash
python examples/python/export_dataset.py YOUR_DATASET_ID --limit 1000
```

This reads an existing Dataset and does not start another Actor run. It writes properties.json and properties.csv. Nested values are JSON strings in CSV; the limit bounds downloaded rows and does not imply the full Dataset was exported.

## FAQ

Does SUCCEEDED mean complete coverage? No: inspect SUMMARY, row count and missing fields. Source availability, budgets and requested limits affect results. Does this download photos? It returns available photo URLs. See [FAQ](docs/faq.md) for timeouts, ZPIDs and partial results.

## Limits and pricing

Verified 2026-10-22: one billable event per saved Dataset record, with no separate start fee. Per 1,000 records: FREE $2.40; BRONZE $1.90; SILVER $1.50; GOLD, PLATINUM and DIAMOND $1.20. Review the [current Actor pricing](https://apify.com/datascraperes/zillow-property-detail-scraper?fpr=edudata) and applicable platform charges before running. Examples set maxTotalChargeUsd=0.02; raising record limits does not raise that budget automatically.

maxResults supports 1–10,000 but does not guarantee delivery of that many records. Building expansion depends on source inventory; community inventory is bounded. Addresses can be ambiguous, fields can be missing, and runs can yield partial results. Inspect before rerunning; a new run can incur new charges.

## Hosted version

Use [Zillow Property Details Scraper](https://apify.com/datascraperes/zillow-property-detail-scraper?fpr=edudata) for the current hosted service. For discovery, see [filtered Zillow searches](https://apify.com/datascraperes/zillow-search-url-scraper?fpr=edudata) or [ZIP-code listings](https://apify.com/datascraperes/zillow-zip-code-scraper?fpr=edudata).

## Responsible use

Respect source terms and applicable privacy requirements. Verify consequential facts against original listings. Estimates and historical samples are not professional valuation advice. This integration is not affiliated with Zillow.

## Support

Report example problems through [GitHub Issues](https://github.com/datacrawler-edu/zillow-property-details-python/issues). For collection issues, use the hosted Actor's Issues tab and include a sanitized input and run ID. Never share tokens.

## License

[MIT](LICENSE) covers this repository's documentation and examples, not hosted-service access or source-data rights.
