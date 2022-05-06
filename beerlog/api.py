from beerlog.core import get_beers_from_database
from beerlog.serializers import BeerOut
from fastapi import FastAPI
from typing import List

api = FastAPI(title="Beerlog")


@api.get('/beers/', response_model=List[BeerOut])
def list_beers():
    beers = get_beers_from_database()
    return beers
