from dagster import Definitions, load_assets_from_modules
from .assets import ingestion, processing, ml_models

all_assets = load_assets_from_modules([ingestion, processing, ml_models])

defs = Definitions(
    assets=all_assets,
    # resources={
    #     "postgres": postgres_resource,
    # },
)
