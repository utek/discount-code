import datetime

from fastapi import FastAPI, HTTPException

from discount_code import codes, models, storage

app = FastAPI()


def validate_discount(discount: models.Discount):
    """Check if user is able to claim this discount"""
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    if discount.start_date > datetime.date.today():
        raise HTTPException(status_code=404, detail="Discount not active")
    if discount.end_date and discount.end_date < datetime.date.today():
        raise HTTPException(status_code=404, detail="Discount expired")
    if discount.count <= 0:
        raise HTTPException(status_code=404, detail="Discount not active")


@app.post("/code/")
async def get_code(get_code_data: models.GetCodeData):
    """Create discount code for provided discount"""
    discount = storage.get_discount(str(get_code_data.discount_id))
    validate_discount(discount)
    code = codes.generate_code()
    code_data = {
        "brand_id": discount.brand_id,
        "code": code,
        "created": datetime.datetime.now(),
        "expire": datetime.datetime.now() + datetime.timedelta(days=discount.valid_for),
        "user_id": get_code_data.user_id,
        "value": discount.value,
    }
    code = storage.save_code(code_data)
    discount.count -= 1
    storage.save_discount(discount.dict())
    return code


@app.post("/discount/")
async def create_discount(discount_data: models.DiscountData):
    """Create discount using provided data"""
    data_dict = discount_data.dict()
    discount = storage.save_discount(data_dict)
    return discount
