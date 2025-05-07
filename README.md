# 🤖 ModelMind Chatbot

**ModelMind Chatbot** is an interactive data analysis assistant built with **Streamlit** and **Google's Gemini API**. It allows users to upload CSV files, ask natural language questions about their data, and receive code-based insights and visualizations. Users can also generate, run, and save Python code for data exploration directly in the app.

---

## 🚀 Features

- 📂 Upload any CSV file for analysis  
- 💬 Chat interface powered by Gemini API  
- 🧠 Get intelligent answers about your dataset  
- 📈 Auto-suggest and generate visualizations  
- 🧾 Execute and save Python code snippets  
- 🗂️ View dataset shape, column names, and preview  
- 🔄 Maintains chat history per session  

---

## 📁 File Structure

```bash
.
├── chatbot_app.py        # Main Streamlit app
├── gemini_chat.py        # Gemini API integration and logic
├── generated_codes/      # Saved Python code snippets
├── README.md             # Project documentation
```

## 🧠 How It Works

![image](https://github.com/user-attachments/assets/e7be9904-e2ca-41fa-ad7c-ac18c6e93810)


## 🧰 Functions Overview
🔹 chatbot_app.py
- Function	Role	Description
- chat_bubble	Rendering	Displays styled chat messages in Streamlit
- load_data	Loading	Loads and fills missing data from CSV
- get_gemini_response	Querying	Gets response from Gemini API

🔹 gemini_chat.py
- Function	Role	Description
- load_data	Loading	Reads and cleans CSV file
- create_prompt	Formulating	Builds structured prompt from question and data
- get_gemini_response	Querying	Sends prompt to Gemini and returns the result

## 🔑 Gemini API Setup
Make sure to set your Gemini API key in gemini_chat.py:
```bash
genai.configure(api_key="YOUR_API_KEY_HERE")
```

## 🛠 Requirements
Install the required Python packages:

```bash
pip install requirements.txt
```

## ▶️ Running the App
Run the Streamlit app locally:

```bash
streamlit run chatbot_app.py
```

## 📄 License
This project is for educational and demo purposes only.

## 🙋‍♀️ Authors
Developed by Drashti – Master's in Data Science @ Pace University

```bash
Let me know if you want this turned into a downloadable `.md` file or customized further for deployment or team use.
```
