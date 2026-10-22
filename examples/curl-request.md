# Start a small run with cURL

From the repository root, with APIFY_TOKEN set in your shell:

```bash
curl --fail-with-body --max-time 45 --request POST \
  'https://api.apify.com/v2/acts/datascraperes~zillow-property-detail-scraper/runs?build=latest&timeout=180&memory=512&maxTotalChargeUsd=0.02' \
  --header "Authorization: Bearer $APIFY_TOKEN" \
  --header 'Content-Type: application/json' \
  --data-binary @data/sample-input.json
```

This starts a run and returns its ID, not property rows. Poll GET /v2/actor-runs/RUN_ID until terminal. Download GET /v2/datasets/DATASET_ID/items?format=json and inspect SUMMARY at GET /v2/key-value-stores/STORE_ID/records/SUMMARY. Replace IDs with those from the returned run. A client timeout can leave the run running: inspect before repeating the POST. Do not share your token. The USD 0.02 limit applies to Actor charges; review current platform costs separately.
