This sample project is using Poetry (https://python-poetry.org/)

Requirements:
    - Python 3.10
    - Poetry

You can run it using following commands:

```
poetry install
poetry run uvicorn discount_code.main:app
```

This will prepare environment for the application and start it.
Application will run on http://127.0.0.1:8000.

This application provides 2 endpoints:

POST /discount/ - Create discount using provided data

brand_id - ID of the brand that creates discount (required) (UUID as string)
count - number of codes that can be created for this discount (if not set then there is no limit of how many codes can be created) (int)
end_date - last day when the codes can be created (date in format YYYY-MM-DD)
start_date - first day when the codes can be created (date in format YYYY-MM-DD)
valid_for - how long the codes for this discount are valid (number in days)
value - value of the discount code (int - percent)

This endpoint return the created discount object.
It contains same fields as mentioned above plus:

create - datetime of creation of the discount
discount_id - id of the created discount

POST /code/ - Create discount code for provided discount

discount_id - ID of the discount that code should be created for (UUID as string)
user_id - ID of the user that requesting the code (UUID as string)

For more details please see http://127.0.0.1:8000/docs (provided by FastAPI
Framework)

