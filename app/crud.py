

from pydantic import BaseModel
from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017")

db = client["carpartdb"]


class Product(BaseModel):
    name: str
    description: str
    quantity: int
    price: float

# Fonction d'ajout, de mise à jour, de suppression et de lecture à écrire ici
# Exemple de fonction d'ajout :
def add_product(product: Product):
    result = db["products"].insert_one(product.dict())
    return str(result.inserted_id)
