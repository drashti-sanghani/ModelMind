import streamlit as st
import os
from gemini_chat import load_data, get_gemini_response

# Constants
CODES_DIR = "generated_codes"
os.makedirs(CODES_DIR, exist_ok=True)

st.set_page_config(page_title="ModelMind Chatbot", layout="centered")
st.title("🔮 ModelMind Chatbot")

# === Sidebar: Upload CSV ===
st.sidebar.header("Upload CSV")
csv_file = st.sidebar.file_uploader("Upload a CSV file", type="csv")

if csv_file:
    df = load_data(csv_file)

    st.sidebar.subheader("Preview")
    st.sidebar.dataframe(df.head())
    st.sidebar.markdown(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
    st.sidebar.markdown("**Columns:** " + ", ".join(df.columns))

    # === Session Initialization ===
    if "history" not in st.session_state:
        st.session_state.history = []
    if "code_response" not in st.session_state:
        st.session_state.code_response = None
    if "code_filename" not in st.session_state:
        st.session_state.code_filename = ""

    # === Chat Bubble HTML Renderer ===
    def chat_bubble(role, content):
        bubble_color = "#DCF8C6" if role == "user" else "#F1F0F0"
        align = "flex-end" if role == "user" else "flex-start"
        name = "🧑‍💻 You" if role == "user" else "🤖 Assistant"
        return f"""
        <div style="display: flex; justify-content: {align}; margin: 10px 0;">
            <div style="
                padding: 10px 15px;
                border-radius: 15px;
                max-width: 70%;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                font-size: 16px;
            ">
                <strong>{name}:</strong><br>{content}
            </div>
        </div>
        """

    # === Show chat history ===
    for msg in st.session_state.history:
        st.markdown(chat_bubble(msg["role"], msg["content"]), unsafe_allow_html=True)

    # === Input Box ===
    user_prompt = st.chat_input("Type your message here...")

    # === On user submit ===
    if user_prompt:
        st.session_state.history.append({"role": "user", "content": user_prompt})

        try:
            response = get_gemini_response(user_prompt, df)
        except Exception as e:
            response = f"⚠️ Error: {e}"

        st.session_state.history.append({"role": "assistant", "content": response})
        st.session_state.code_response = None

        # Optional: Extract code if needed
        if "```" in response:
            code = response.split("```")[1]
            st.session_state.code_response = code.strip()

        st.rerun()  # Force rerun to display latest updates

    # === Show Latest Code (Optional) ===
    if st.session_state.history and st.session_state.history[-1]["role"] == "assistant":
        if st.session_state.code_response:
            st.code(st.session_state.code_response, language="python")

            with st.expander("💾 Save this code?"):
                filename = st.text_input("Enter filename (no .py):", value=st.session_state.code_filename or "script1")
                if st.button("✅ Save Code"):
                    safe_name = "_".join(filename.strip().split())
                    filepath = os.path.join(CODES_DIR, f"{safe_name}.py")
                    with open(filepath, "w") as f:
                        f.write(st.session_state.code_response)
                    st.success(f"Code saved to `{filepath}`")
                    st.session_state.code_filename = safe_name

else:
    st.info("📂 Please upload a CSV file to get started.")
