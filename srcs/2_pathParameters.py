from enum import Enum
from fastapi import FastAPI

app = FastAPI()

# declare path "parameters"
@app.get("/items/{item_id}")
# declare the type of a path parameter
async def read_item(item_id: int): 
  return {"item_id: item_id"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

# Not called When user_id == me
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# match first call
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

# no error occur but not called
@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

# inherits str
class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"

# predefined values with Enum class
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
  if model_name is ModelName.alexnet:
    return {"model_name": model_name, "message": "Deep Learning FTW!"}
  return {"model_name": model_name, "message": "Have some residuals"}

# Path convertor
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
