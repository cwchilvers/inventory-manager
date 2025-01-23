from fastapi import FastAPI
from models.item import Item

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Success"}

inventory = []

# Get inventory
@app.get("/inventory")
async def get_inventory():
    return {"inventory": inventory}

# Get item
@app.get("/inventory/{item_id}")
async def get_item(item_id: int):
    for item in inventory:
        if item.id == item_id:
            return {"item": item}
    return {"message": "Item not found"}

# Add item
@app.post("/inventory")
async def add_item(item: Item):
    inventory.append(item)
    return {"message": "Added item"}

# Remove item
@app.delete("/inventory/{item_id}")
async def delete_item(item_id: int):
    for item in inventory:
        if item.id == item_id:
            inventory.remove(item)
            return {"message": "Item deleted"}
    return {"message": "Item not found"}

# Update item
@app.put("/inventory")
async def update(item_id: int, item_obj: Item):
    for item in inventory:
        if item.id == item_id:
            item.id = item_id
            item.item = item_obj.item
            return {"item": "item"}
    return {"message": "Item not found"}