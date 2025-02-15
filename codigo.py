import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()


st.set_page_config(page_title="Chat Legal", page_icon="🤖", layout="wide")
st.title("Chat Legal")


@st.cache_resource
def load_model():
    return GoogleGenerativeAI(model="gemini-pro", temperature=0.7)

llm = load_model()
prompt = ChatPromptTemplate.from_template("Responda a seguinte pergunta com excelência: {user_input}")
model = prompt | llm

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_area("Digite sua pergunta", "")

if st.button("Enviar") and user_input.strip():
    with st.spinner("Gerando resposta..."):
        response = model.invoke({"user_input": user_input})
    
    st.session_state.chat_history.append(("Você", user_input))
    st.session_state.chat_history.append(("Chat Legal", response))
    
    for sender, message in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {message}")
