from typing import List, Optional
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

def delete(id:int) -> bool:
    for idx, quote in enumerate(ai_quotes):
        if quote['id']==id:
            del ai_quotes[idx]
            return True
    return False