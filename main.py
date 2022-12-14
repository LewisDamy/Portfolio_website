from typing import Union
from datetime import datetime


from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel



class Category(BaseModel):
    name: str
    description: Union[str, None] = None


now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

########    API CODE    ########

app = FastAPI()

class Item(Category):
    """
    Base class for Items
    """
    # item_id: Union[UUID, None] = None
    name: Union[str, None] = None
    description: Union[str, None] = None 
    price: Union[float, None] = None
    tax: float = 10.5
    tags: list[str] = []
    datestamp: Union[str, None] = None

class Type(Category):
    """

    """
    id: int
    name: str
    description: Union[str, None] = None

class Category(BaseModel):
    """
    Class for Category of each Item
    """
    id: int
    name: str
    item: Union[Item, None] = None


# class Item(BaseModel):
#     """
#     Base class for Items
#     """
#     # item_id: Union[UUID, None] = None
#     name: Union[str, None] = None
#     description: Union[str, None] = None 
#     price: Union[float, None] = None
#     tax: float = 10.5
#     tags: list[str] = []
#     datestamp: Union[str, None] = None    

### FAKE DATABASES ###
items = {   
            "foo": {"name": "Foo", "price": 50.2}, 
            "bar": {"name": "Bar", "description": "The bartenders", "price": 50.2, "tax": 20.2}, 
            "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

categories = {}

categorized_items = []


### API Requests for CATEGORIZED_ITEMS ###


@app.post("/category/item/")##, response_model=Category, Item)
async def create_item_with_category(category: Category, item: Item):
    # if category.name in categories:
        item.datestamp = dt_string
        items[item.name] = item
        result = { "category_id": category, "item": item }
        categorized_items.append(result)
        return result
    # else:   # category not found
        # raise HTTPException

@app.get("/category/items/")
async def get_categorized_items():
    return categorized_items





### API Requests for items ###

@app.post("/items/", response_model=Item)           # create item
async def create_item(item: Item):
    item.datestamp = dt_string
    # catch error in here <?> for duplicated item
    items[item.name] = item
    return item

@app.get("/items/")                                 # list all 
async def return_items():
    return items

@app.get("/items/{item_id}", response_model=Item)   # list specific item
async def read_item(item_id: str):
    return items[item_id]

@app.put("/items/{item_id}", response_model=Item)   # update item
async def update_item(item_id: str, item: Item):
    update_item_encoded =  jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded

@app.delete("/items/{item_id}", status_code=200)    # delete item
async def delete_item(item_id: str):
    items.pop(item_id)
    return item_id


### API Requests for CATEGORIES  ###

@app.post("/category/", response_model=Category)
async def create_category(category: Category):
    # catch error in here <?> for duplicated item
    categories[category.name] = category
    return category

# @app.post("/category/")
# async def create_category(category: Category):
#     return category

@app.put("/category/{category_id}")
async def create_category(category_id: int, category: Category):
    return {"category_id": category_id, **category.dict()}

@app.get("category/{category_id}")
async def get_category(category_id):
    return {"category_id": category_id }

@app.get("/categories/")
async def get_categories():
    return categories