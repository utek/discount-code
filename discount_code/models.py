import datetime
import uuid
from typing import Optional

from pydantic import BaseModel, condecimal


class DiscountData(BaseModel):
    brand_id: uuid.UUID
    count: Optional[int] = None
    end_date: Optional[datetime.date] = None
    start_date: Optional[datetime.date] = None
    valid_for: Optional[int] = 30
    value: condecimal(gt=0)


class GetCodeData(BaseModel):
    discount_id: uuid.UUID
    user_id: uuid.UUID


class Discount(DiscountData):
    discount_id: uuid.UUID
    created: datetime.datetime


class DiscountCode(BaseModel):
    brand_id: uuid.UUID
    code: str
    created: datetime.datetime
    end_date: Optional[datetime.date] = None
    user_id: uuid.UUID
    value: condecimal(gt=0)
