"""Small hosted Apify API helper. Uses only Python standard library."""
import json,os,time
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urlencode,quote
from urllib.error import HTTPError
BASE='https://api.apify.com/v2/'
ACTOR='datascraperes~zillow-property-detail-scraper'
TERMINAL={'SUCCEEDED','FAILED','ABORTED','TIMED-OUT'}
def api(path,body=None):
    token=os.environ['APIFY_TOKEN']
    req=Request(BASE+path,data=None if body is None else json.dumps(body).encode(),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
    with urlopen(req,timeout=45) as response:
        value=json.load(response)
    return value.get('data',value) if isinstance(value,dict) else value
def dataset_rows(dataset_id,limit=1000):
    rows=[]
    while len(rows)<limit:
        page=api('datasets/'+quote(dataset_id,safe='')+'/items?'+urlencode({'format':'json','offset':len(rows),'limit':min(100,limit-len(rows))}))
        if not page:break
        rows.extend(page)
    return rows
def collect(run_input,prefix='property-details'):
    # Do not retry a start request blindly: an acknowledgement may have been lost.
    query=urlencode({'build':'latest','timeout':180,'memory':512,'maxTotalChargeUsd':0.02})
    run=api('acts/'+ACTOR+'/runs?'+query,run_input)
    run_id=run['id'];print('Run ID:',run_id,flush=True)
    Path(prefix+'-run.json').write_text(json.dumps(run,indent=2),encoding='utf-8')
    deadline=time.monotonic()+240
    while run['status'] not in TERMINAL:
        if time.monotonic()>=deadline:
            raise TimeoutError('Local wait ended. Inspect run '+run_id+' before starting another run.')
        time.sleep(3)
        run=api('actor-runs/'+run_id)
    rows=dataset_rows(run['defaultDatasetId'],run_input.get('maxResults',100))
    summary=None
    try:summary=api('key-value-stores/'+run['defaultKeyValueStoreId']+'/records/SUMMARY')
    except HTTPError as exc:
        if exc.code!=404:raise
    Path(prefix+'-rows.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    Path(prefix+'-run.json').write_text(json.dumps({'run':run,'summary':summary},indent=2),encoding='utf-8')
    print(json.dumps({'runId':run_id,'runStatus':run['status'],'summary':summary,'rows':len(rows)},indent=2))
    if run['status']!='SUCCEEDED':
        raise RuntimeError('Run ended '+run['status']+'; available rows were saved. Inspect before retrying.')
    return rows
