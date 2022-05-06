from beerlog.core import get_beers_from_database
from beerlog.serializers import BeerIn, BeerOut
from beerlog.database import get_session
from beerlog.models import Beer
from fastapi import FastAPI
from typing import List

api = FastAPI(title="Beerlog")


@api.get('/beers/', response_model=List[BeerOut])
def list_beers():
    beers = get_beers_from_database()
    return beers


# payload - o que mandamos de dados na nossa requisicao
@api.post('/beers/', response_model=BeerOut)
def add_beer(beer_in: BeerIn):
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        # add a beer no db
        session.add(beer)
        session.commit()
        # recupera os id quando inserida a beer
        session.refresh(beer)
    return beer
