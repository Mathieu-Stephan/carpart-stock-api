from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017")
db = client["carpartdb"]


class Product(BaseModel):
    name: str
    description: str
    quantity: int
    price: float


app = FastAPI()

# Ajout d'un produit
@app.post("/products/")
async def create_product(product: Product):
    result = db["products"].insert_one(product.dict())
    return {"id": str(result.inserted_id)}

# Modifier un produit (descriptif, ajouter/reduire la quantité)
@app.put("/products/{product_id}")
async def update_product(product_id: str, updated_product: Product):
    result = db["products"].update_one({"_id": ObjectId(product_id)}, {"$set": updated_product.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product updated"}

# Supprimer un produit
@app.delete("/products/{product_id}")
async def delete_product(product_id: str):
    result = db["products"].delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}

# Accéder au descriptif d'un produit et à la quantité
@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    product = db["products"].find_one({"_id": ObjectId(product_id)})
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Accéder à la liste des produits
@app.get("/products/", response_model=List[Product])
async def get_products():
    products = db["products"].find()
    return list(products)

