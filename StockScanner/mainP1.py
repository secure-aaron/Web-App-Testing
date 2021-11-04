from fastapi import FastAPI
#import uvicorn

app = FastAPI()

# Root Request
@app.get("/")
async def read_root():
    return {"Hello": "World"}


# Get --> Read Todo
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item id": item_id, "q": q}
   


#uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True) # ENABLE RELOAD FOR DEBUGGING. DISABLE FOR PRODUCTION.

