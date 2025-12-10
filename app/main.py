from fastapi import FastAPI, Path, Query
from typing import List
from sqlalchemy import func
from sqlalchemy.orm import Session


from app.database import get_db, engine, Base
from app.models import Product

app = FastAPI()
Base.metadata.create_all(engine)

@app.get('/products')
async def get_products():
    db: Session = get_db()
    product_list = []
 
    for product in db.query(Product).all():
        product_list.append(product.to_dict())
        
    return {'products': product_list}


# 3.2 GET/products/{product_id}
# Databasedan productlar olindi va berilgan id dagi product borligi 
# tekshirildi bo'lsa chiqarildi bo'lmasa malumot topilmadi deyiladi
@app.get("/products/{product_id}")
async def get_product_by_id(product_id: int):
   with get_db() as session:
        products = session.query(Product).all()
        for i in products:
            if i.product_id == product_id:
                return i.to_dict()
    
        else:
            return {"Message":"Product topilmadi"}


# 3.3  GET /products/search

@app.get("/products/search/")
async def search_product_by_name(name : str):
    db: Session = get_db()
    search = f"%{name.lower()}%"
   
    search_product = db.query(Product).filter(func.lower(Product.name).ilike(search)).all()
    return search_product

# Bunda func.lower ishlatildi sababi bu sqlalchemy lowerni tanimaydi



# 3.4  GET /products/filter/category

@app.get("/products/filter/category/")
async def filter_by_category(category: str):
    db: Session = get_db()

    category = f"%{category.lower()}%"
   
    search_category = db.query(Product).filter(func.lower(Product.category).ilike(category)).all()
    return search_category
    
     

# 3.5  GET /products/filter/price

@app.get("/products/filter/price/")
async def filter_by_price(min_price: float = Path(gt=0),
                          max_price: float = Path(gt=0)):
    db: Session = get_db()
    filter_products = db.query(Product).filter(Product.price >= min_price,Product.price <= max_price).all()
    return filter_products


# 3.6  GET /products/paginated

@app.get("/products/filter/price/")
async def paginate_products(limit: int = Query(10,gt=0),
                          offset: int = Query(0,ge=0)):
    db: Session = get_db()
    products = db.query(Product).limit(limit).offset(offset).all()
    return products
   


