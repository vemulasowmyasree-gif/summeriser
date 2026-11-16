from llm_main import summarizer

from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class summarizerRequest(BaseModel):
    paragraph:str

@app.post("/summarizersend_point")
def summarizer_user(user_input:summarizerRequest):
    print(user_input.paragraph)
    res=summarizer(user_input.paragraph)
    print(res)
    return{
        "data":res
    } 