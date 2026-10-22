"""Enrich identifiers from an existing Dataset, bounded to five records."""
import argparse
from hosted import collect
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('dataset_id');args=parser.parse_args()
    collect({'startUrls':[],'addresses':[],'propertyStatus':'FOR_SALE','extractBuildingUnits':'disabled','searchResultsDatasetId':args.dataset_id,'maxResults':5},prefix='enriched-properties')
