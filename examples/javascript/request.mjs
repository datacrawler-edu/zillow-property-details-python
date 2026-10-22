// Start only. Read the returned run ID; do not assume the run has completed.
import {readFile} from 'node:fs/promises';
if (!process.env.APIFY_TOKEN) throw new Error('Set APIFY_TOKEN');
const input=JSON.parse(await readFile(new URL('../../data/sample-input.json',import.meta.url),'utf8'));
const response=await fetch('https://api.apify.com/v2/acts/datascraperes~zillow-property-detail-scraper/runs?build=latest&timeout=180&memory=512&maxTotalChargeUsd=0.02',{
  method:'POST',headers:{Authorization:`Bearer ${process.env.APIFY_TOKEN}`,'Content-Type':'application/json'},body:JSON.stringify(input),signal:AbortSignal.timeout(45000)
});
if (!response.ok) throw new Error(`Apify HTTP ${response.status}; inspect existing runs before retrying`);
const {data:run}=await response.json();
console.log(JSON.stringify({runId:run.id,status:run.status,datasetId:run.defaultDatasetId},null,2));
console.log('Poll GET /v2/actor-runs/'+run.id+' until terminal, then inspect SUMMARY and Dataset rows. A client timeout does not abort the run.');
