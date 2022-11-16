import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI

from auth import auth_router


# Load env variables from .env file.
load_dotenv()


app = FastAPI()
app.include_router(auth_router, prefix='/auth')

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, log_level="info", reload=True)
