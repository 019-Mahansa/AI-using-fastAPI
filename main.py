from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from google import genai
from dotenv import load_dotenv
import markdown
# from pydantic import BaseModel
load_dotenv()


app = FastAPI()
templates = Jinja2Templates(directory = "templates")
client = genai.Client()

app.mount("/static", StaticFiles(directory="templates"), name = "static")
# class Question(BaseModel):
#     question : str

# @app.get("/")
# def say_hello():
#     return {"message" : "hello"}

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Insiden Challenger",
    )
    html_respose = markdown.markdown(response.text)
    return templates.TemplateResponse("index.html",{"request": request, "answare": html_respose})

