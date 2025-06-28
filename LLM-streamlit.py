import streamlit as st
from langchain_openai import ChatOpenAI

st.title("LLM via streamlit Test")

# ChatOpenAPI referrence
# https://python.langchain.com/docs/integrations/chat/openai/

def generate_response(input_text):
  # LM Studioのローカルエンドポイントを指定
  llm = ChatOpenAI(
    base_url="http://minihiro.ddo.jp:31875/v1",
    api_key="None",  # ローカルLLMではAPIキーは不要
    temperature=0.7,
    model="google/gemma-3-12b",  # 使用するモデル名を指定
  )
  st.info(llm.invoke(input_text).content)

with st.form("my_form"):
  text = st.text_area(
    "質問を入力してください:",
    "日本の首都の特徴にはどんなものがありますか？",
  )
  submitted = st.form_submit_button("Submit")
  if submitted:
    generate_response(text)