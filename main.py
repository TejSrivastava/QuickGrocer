from fastapi import FastAPI, Path
from typing import Optional

app=FastAPI()

#An endpoint is the point of entry in a
#communication channel when two systems are interacting.
#It refers to touchpoints of the communication
#between an API and a server.

#/hello
#/get-item

#localhost/hello

#GET
#POST
#PUT
#DELETE

@app.get("/")
def home():
    return{"Data":"Testing"}

@app.get("/about")
def about():
    return{"Data":"About"}

inventory= {
    1:{
        "Name":"Milk",
        "Price":3.99,
        "Brand":"Nandini"
    }
}

#Path Parameter
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you would like to view")):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: Optional[str] =None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return{"Data": "Not found"}

