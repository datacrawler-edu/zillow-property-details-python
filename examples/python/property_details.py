"""One known property: result ceiling 1, event budget USD 0.02."""
import json
from pathlib import Path
from hosted import collect
if __name__=='__main__':
    collect(json.loads((Path(__file__).resolve().parents[2]/'data/sample-input.json').read_text(encoding='utf-8')))
