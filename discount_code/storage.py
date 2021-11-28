import datetime
import uuid

from discount_code import models

discounts = {
    "d2f01ce9-7c45-42fe-9bd6-b447ffd5b669": models.Discount(
        **{
            "brand_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "count": 10,
            "end_date": "2021-12-24",
            "start_date": "2021-11-28",
            "valid_for": 30,
            "value": 30,
            "discount_id": "d2f01ce9-7c45-42fe-9bd6-b447ffd5b669",
            "created": "2021-11-28T21:11:54.646466",
        }
    ),
}

discounts_codes = []


def get_discount(discount_id: str):
    discount = discounts.get(discount_id, None)
    if not discount:
        return None
    return discount


def save_code(code_data: dict):
    discount_code = models.DiscountCode(**code_data)
    discounts_codes.append(discount_code)
    return discount_code


def save_discount(discount_data: dict):
    discount_id = discount_data.get("discount_id", None)
    if not discount_id:
        discount_data["created"] = datetime.datetime.now()
        discount_id = uuid.uuid4()
        discount_data["discount_id"] = discount_id
    discount = models.Discount(**discount_data)
    discounts[str(discount_id)] = discount
    return discount
