from fastapi import FastAPI
from sqlalchemy.orm import Session

from .database import get_db, engine, Base
from .models import Product

app = FastAPI()

Base.metadata.create_all(engine)


@app.get('/products')
def get_products():
    db: Session = get_db()

    product_list = []
    count = 0
    for product in db.query(Product).all():
        product_list.append(product.to_dict())
        count += 1

    return {'products': product_list, 'count': count}

