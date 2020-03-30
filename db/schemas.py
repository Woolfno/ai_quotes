from pydantic import BaseModel


class QuoteBase(BaseModel):
    author: str
    quote: str

class QuoteCreate(QuoteBase):
    pass

class Quote(QuoteBase):
    id: int