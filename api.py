from fastapi import FastAPI, Request
from pydantic import BaseModel
import pandas as pd
import google.generativeai as genai
import os

# === Initialize Gemini API ===
genai.configure(api_key=os.getenv("AIzaSyDf-61fNcKDOOxoC1ze0E1d3VvP8s9H6Ro"))
model = genai.GenerativeModel("gemini-2.0-flash")

# === FastAPI Setup ===
app = FastAPI()

# === Request Schema ===
class QueryRequest(BaseModel):
    question: str
    data: dict  # The DataFrame as a dictionary

# === Response Route ===
@app.post("/ask")
async def ask_model(query: QueryRequest):
    try:
        df = pd.DataFrame(query.data)
        # Create a prompt that includes a sample of the data
        prompt = f"You are a data analyst. The user uploaded the following data:\n\n{df.head(5).to_markdown()}\n\nQuestion: {query.question}"

        response = model.generate_content(prompt)
        return {"response": response.text.strip()}

    except Exception as e:
        return {"response": f"❌ Error processing request: {str(e)}"}
