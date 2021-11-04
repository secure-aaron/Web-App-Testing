from fastapi import FastAPI


app = FastAPI()

# Root Request
@app.get("/", tags=['ROOT']) # Specify tags for generated documentation.
async def root() -> dict: # Puts json compatible data into a dictionary which is used to send a response to the client.
    return print.("<h1>About Page</h1>")


# Get --> Read Todo
@app.get('/todo', tags =['todos'])
async def get_todo() -> dict:
    return {"data": todos} # This data can be pretty much anything including different databases as well.
    # In this case we have the json data below.


# Post --> Create Todo
@app.post('/todo', tags =['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": "A todo has been added successfully!"
    }
 

# Put --> Update Todo
@app.put('/todo/{id}', tags =['todos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Activity'] = body['Activity']
            
            return {
                "data":f"Todo with id {id} has been updated."
            }
    return {
        "data":f"Todo this id number {id} was not found!"
    }


# Delete --> Delete Todo
@app.delete('/todo/{id}', tags =['todos'])
async def delete_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todos.remove(todo)
            return {
                "data":f"Todo with id {id} has been deleted."
            }
    return {
        "data":f"Todo this id number {id} was not found!"
    }

# Current todos list
todos = [
    {"id": "1",
    "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
    "id": "2",
    "Activity": "Writing 3 pages of my new book at 2:00 PM."
    }
]


