import sys

import pathlib
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI


# Load env variables from .env file.
load_dotenv()

app = FastAPI()

# Append path to current dir to sys.path.
current_dir = pathlib.Path(__file__).parent.resolve()
sys.path.append(str(current_dir))


@app.get('/')
def test_route():
    return {'ok': True, 'status_code': 200}


def add_routers():
    """Add routes from all project directories to app here."""
    pass


if __name__ == "__main__":
    add_routers()
    uvicorn.run('main:app', host="0.0.0.0", port=8000, log_level="info", reload=True)
