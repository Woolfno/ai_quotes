from typing import List
from fastapi import FastAPI, status, Response
from db.schemas import QuoteCreate, Quote
from db import crud


app = FastAPI()


@app.post('/quotes/', 
        description='Create ai quote.', 
        response_model=Quote, 
        status_code=status.HTTP_201_CREATED)
def create_quote(quote:QuoteCreate):
    return crud.create_quote(quote)

@app.put('/quotes/{quote_id}', 
        description="Update ai quote.",
        response_model=Quote, 
        responses={status.HTTP_201_CREATED:{'description': 'Quote created.'}})
def update_quote(quote_id:int, quote:Quote, response:Response):
    quote,status = crud.update_quote(quote)
    response.status_code = status
    return quote

@app.get('/quotes/', 
        description='Read limit quotes.', 
        response_model=List[Quote])
def read_quotes(skip:int=0, limit:int=10):
    return crud.get_quotes(skip=skip, limit=limit)

@app.get('/quotes/{quote_id}', 
        description='Read quote by id.', 
        response_model=Quote,
        responses={status.HTTP_404_NOT_FOUND:{'description': 'Quote not fount.'}})
def read_quote(quote_id:int, response:Response):
    if not crud.get_quote(quote_id):
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    return crud.get_quote(quote_id)

@app.delete('/quotes/{quote_id}', 
        description='Delete quote by id.', 
        responses={status.HTTP_404_NOT_FOUND:{'description': 'Quote not fount.'}})
def delete(quote_id:int, response:Response):
    if not crud.delete(quote_id):
        response.status_code=status.HTTP_404_NOT_FOUND
    response.status_code=status.HTTP_200_OK
    return response