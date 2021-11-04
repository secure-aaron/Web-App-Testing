import uvicorn


# Minimal app - get request. Run if the main file in the app directory is app.
if __name__ == "__main__":
    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True) # ENABLE RELOAD FOR DEBUGGING. DISABLE FOR PRODUCTION.








