from pydantic import BaseModel
from typing import List, Dict

class Inventory(BaseModel):
    location: str
    inventory: Dict[str, int]

class StockSubmission(BaseModel):
    inventoryDate: str
    records: List[Inventory]
