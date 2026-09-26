from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from model import CLIPModel
from search import ShoeSearch


app = FastAPI(
    title="Shoe Search API"
)

app.mount(
    "/shoes",
    StaticFiles(directory="shoes"),
    name="shoes"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

clip_model = CLIPModel()

shoe_search = ShoeSearch()


class SearchRequest(BaseModel):
    query: str
    top_k: int = 10


@app.get("/")
def root():
    return {
        "message": "Shoe Search API is running"
    }


@app.post("/search")
def search_shoes(request: SearchRequest):
    embedding = clip_model.encode_text(
        request.query
    )

    results = shoe_search.search(
        embedding,
        request.top_k
    )

    return {
        "query": request.query,
        "results": results
    }
