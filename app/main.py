from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()  

templates = Jinja2Templates(directory="templates"),

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

@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")
