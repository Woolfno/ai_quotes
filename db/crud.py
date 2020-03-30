from typing import List, Optional, Tuple
from .models import ai_quotes
from .schemas import QuoteCreate, Quote


def get_quote(id:int) -> Optional[Quote]:
    for quote in ai_quotes:
        if quote['id']==id:
            return quote
    return None

def get_quotes(skip:int=0, limit:int=10) -> List[Quote]:
    return ai_quotes[skip:limit]

def create_quote(quote:QuoteCreate) -> Quote:
    id = ai_quotes[-1]['id'] + 1
    ai_quotes.append({
        'id': id,
        **quote.dict()
    })
    return ai_quotes[-1]

def update_quote(quote:Quote) -> Tuple[Quote, int]:
    for item in ai_quotes:
        if item['id']==quote.id:
            item['author']=quote.author
            item['quote']=quote.quote
            return quote, 200
    ai_quotes.append(**quote.dict())
    return quote, 201

def delete(id:int) -> bool:
    for idx, quote in enumerate(ai_quotes):
        if quote['id']==id:
            del ai_quotes[idx]
            return True
    return False