import streamlit as st
from user import session_prompt,ask, append_interaction_to_chat_log

st.set_page_config(page_title="Munshi: AI Chatbot", page_icon=":guardsman:", layout="wide")

def chat_bot(question):
    global chat_log
    #print("question=",question)
    answer = ask(question, chat_log)
    chat_log = append_interaction_to_chat_log(question, answer, chat_log)
    #print("answer=",answer)
    return answer

chat_log = session_prompt

st.title("Munshi: AI Chatbot")
st.markdown("Chat with Munshi, an AI chatbot powered by OpenAI.")

query = st.text_input("Query")
if query:
    response = chat_bot(query)
    st.write(response)

    
    