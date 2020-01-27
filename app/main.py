from fastapi import FastAPI

from app.resources import strings
from app.schemas.bulletin import Bulletin

app = FastAPI()


@app.get("/", response_model=Bulletin)
async def get_root() -> Bulletin:
    return Bulletin(
        name="Gophers <3", description="golang mascot", links=[strings.gopher_link],
    )
