from typing import List
from fastapi import FastAPI, Response, status
from db.schemas import QuoteCreate, Quote, Message
from db import crud


app = FastAPI()

@app.post('/quotes/', description='Create ai quote', 
        response_model=Quote, status_code=status.HTTP_201_CREATED)
def create_quote(quote:QuoteCreate):
    return crud.create_quote(quote)

@app.get('/quotes/', description='Read limit quotes', 
        response_model=List[Quote])
def read_quotes(skip:int=0, limit:int=10):
    return crud.get_quotes(skip=skip, limit=limit)

@app.get('/quotes/{quote_id}', description='Read quote by id', 
        response_model=Quote, status_code=status.HTTP_200_OK,
        responses={status.HTTP_404_NOT_FOUND:{}})
def read_quote(quote_id:int, response:Response):
    if not crud.get_quote(quote_id):
        response.status_code = status.HTTP_404_NOT_FOUND
        # response.content = {"message": "Quote not found"}
        return
    return crud.get_quote(quote_id)

@app.delete('/quotes/{quote_id}', description='Delete quote by id', 
        response_model=bool, status_code=status.HTTP_200_OK)
def delete(quote_id:int):
    return crud.delete(quote_id)