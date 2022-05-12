from typing import List

from fastapi import FastAPI, Response, status

from beerlog.core import get_beers_from_database
from beerlog.database import get_session
from beerlog.models import Beer
from beerlog.serializers import BeerIn, BeerOut

api = FastAPI(title="Beerlog")


@api.get('/beers', response_model=List[BeerOut])
async def list_beers():
    '''List beers in database'''
    beers = get_beers_from_database()
    return beers


@api.post('/beers', response_model=BeerOut)
async def add_beer(beer_in: BeerIn, response: Response):
    """payload - o que mandamos de dados na nossa requisicao"""
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        # add a beer no db
        session.add(beer)
        session.commit()
        # recupera os id quando inserida a beer
        session.refresh(beer)

        response.status_code = status.HTTP_201_CREATED
    return beer
