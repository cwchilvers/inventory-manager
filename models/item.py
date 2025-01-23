from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Item(BaseModel):
    id: int
    name: str
    category: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    year: Optional[int]
    serial_number: Optional[str]
    quantity: Optional[int]
    price: Optional[float]
    location: Optional[str]
    condition: Optional[str]
    date_added: Optional[datetime] = datetime.utcnow
    descriptions: Optional[str]
    photos: Optional[List[str]] = []
