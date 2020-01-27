from typing import List

from pydantic import BaseModel, Field
from pydantic.networks import AnyHttpUrl

MAX_LENGTH_OF_NAME = 200
MAX_LENGTH_OF_DESCRIPTION = 1000
MAX_LINKS_IN_BULLETIN = 3


class Bulletin(BaseModel):
    name: str = Field(..., max_length=MAX_LENGTH_OF_NAME)
    description: str = Field("", max_length=MAX_LENGTH_OF_DESCRIPTION)
    links: List[AnyHttpUrl] = Field([], max_items=MAX_LINKS_IN_BULLETIN)
