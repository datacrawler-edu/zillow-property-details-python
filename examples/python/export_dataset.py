"""Export an existing Dataset; does not launch or charge for a new Actor run."""
import argparse,csv,json
from pathlib import Path
from hosted import dataset_rows
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('dataset_id');parser.add_argument('--limit',type=int,default=1000);args=parser.parse_args()
    if not 1<=args.limit<=10000:parser.error('--limit must be between 1 and 10000')
    rows=dataset_rows(args.dataset_id,args.limit)
    Path('properties.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    keys=sorted({k for row in rows for k in row})
    with open('properties.csv','w',newline='',encoding='utf-8') as stream:
        writer=csv.DictWriter(stream,fieldnames=keys);writer.writeheader()
        for row in rows:writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()})
    print('Exported',len(rows),'rows; capped by --limit. No new Actor run.')
