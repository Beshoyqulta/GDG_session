import google.generativeai as genai 
import os 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import *
genai.configure(api_key="AIzaSyCh3NzvLSZcnOLFqy27w3yl5pDhzIW7f10")
model = genai.GenerativeModel('gemini-1.5-flash')
app = FastAPI()

class TranslationRequest(BaseModel):
    input: str

def translate_text(input: str):
    response = model.generate_content(
        f"translate the text from English to Arabic and return the only translated text: {input}"
    )
    return response.text
@app.post("/translate/")
async def translate(request: TranslationRequest):
    try:
        translated_text = translate_text(request.input)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



