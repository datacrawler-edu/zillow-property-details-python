# FAQ

## Does this run a scraper on my computer?

The examples call the hosted Apify Actor. You need an Apify account and token. The MIT license covers this repository, not the hosted service or source data.

## Can I enter only a ZPID?

Use a valid listing URL, an exact address, or a Dataset containing positive ZPIDs. There is no independent direct-ZPID input field.

## Are contact information and estimates guaranteed?

No. Fields depend on source availability. An estimate is not a professional valuation. Photo fields contain URLs.

## Is SUCCEEDED proof that everything was found?

No. Check SUMMARY and rows; runs can stop at a result or spending limit and source failures can leave partial results. Preserve the run ID and inspect before retrying. A retry is a new potentially billable run.

## Does a local wait timeout stop a run?

No. The helper prints its run ID before polling and does not automatically abort or repeat it. Inspect that run in Apify; the server-side timeout and spending limit still apply.

## Is CSV a full representation of nested objects?

The Python export serializes nested values as JSON strings. Use the JSON download for structured downstream processing.
