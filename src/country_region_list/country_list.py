import csv
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional, Tuple


data_dir = Path(__file__).parent / "data"


# @lru_cache(1)
# def available_languages() -> List[str]:
#     return sorted(x.name for x in data_dir.iterdir() if (x / "country.csv").exists())


@lru_cache()
def all_countries() -> Tuple[str, str]:
    path = data_dir / "country.csv"
    with path.open() as file_:
        return [(row["id"], row["value"]) for row in csv.DictReader(file_)]

@lru_cache()
def all_regions() -> Tuple[str, str]:
    path = data_dir / "gds-amchart-mapping.csv"
    with path.open() as file_:
        result = [ (row["amchart_id"],row['geodatasource_region']) for row in csv.DictReader(file_)]
        return sorted(result, key = lambda  x: x[1])
# print(countries_for_language())
# print(all_regions())