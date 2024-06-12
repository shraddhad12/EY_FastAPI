from fastapi import FastAPI
from app.views import my_view
import uvicorn

app = FastAPI()

app.include_router(my_view.router)

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)
