# gemini_chat.py

import pandas as pd
import google.generativeai as genai
import os

# Set your Gemini API key
genai.configure(api_key="enter_your_gemini_api")

# Load your CSV data
def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df.fillna("N/A", inplace=True)  # Avoid NaN values
    return df

# Create the prompt from user input and data
def create_prompt(user_question, df):
    # Convert DataFrame to a simple text table or summary
    data_summary = df.head(5).to_string(index=False)
    prompt = f"""You are a helpful data assistant. A user asked a question based on the following data:

{data_summary}

Question: {user_question}
Answer:"""
    return prompt

# Get Gemini response
def get_gemini_response(user_question, df):
    prompt = create_prompt(user_question, df)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
