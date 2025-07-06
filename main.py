# D:\Python\Multiverse\main.py

from Backend import config 

from fastapi import FastAPI
from Backend.route import router

app = FastAPI(title="AI Agent Backend")
app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Multiverse API!"}

# You can keep this for direct running, but the CLI command 'uvicorn main:app' is preferred
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=9999, reload=True)