from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()  

posts: list[dict] = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the content of the first post.",
        "author": "John Doe"
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the content of the second post.",
        "author": "Jane Smith"
    }
]
posts.append(
    {
        "id": 3,
        "title": "Third Post",
        "content": "This is the content of the third post.",
        "author": "Alice Johnson"
    }
)

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home():
    # return {"message": "Welcome to the FastAPI Blog yo!"}
    return f"<h1>{posts[1]['title']}</h1>"


