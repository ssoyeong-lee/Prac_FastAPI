from fastapi import FastAPI

app = FastAPI() #create instance

# path = endpoint = route
# Define a path operation decorator
@app.get("/") 
async def root(): # FastAPI에 의해 호출됨
  return {"messege": "Hello FastAPI World!!!"}