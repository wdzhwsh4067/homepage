from openai import OpenAI
import streamlit as st
import dotenv
import os
# Load environment variables from .env file
dotenv.load_dotenv()
st.set_page_config(layout="wide")

# LOGO_URL_LARGE="./static/lora.png"
st.logo(
    "./static/logo1.png",
    link="https://nicedata.eu.org/"
)

with st.sidebar:
    openai_api_key = st.text_input("API Key", key="chatbot_api_key", type="password")
    "[Get an  API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Wang")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()

    client = OpenAI(
    api_key=os.environ.get("SOTA_API_KEY"),
    base_url=os.environ.get("SOTA_API_BASE")
)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model=os.environ.get("SOTA_API_MODEL"), messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
