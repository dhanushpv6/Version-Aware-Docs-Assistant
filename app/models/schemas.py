from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=3)
    product: str = "sample-product"
    version: str = Field(min_length=1)


class Citation(BaseModel):
    document: str
    section: str
    version: str
    chunk_id: str


class AskResponse(BaseModel):
    answer: str
    citations: list[Citation] = []
    abstained: bool = False
