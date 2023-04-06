# from flask import Flask, request, session,jsonify
# import gradio as gr
# from user import session_prompt,ask, append_interaction_to_chat_log
# #import win32file as fcntl

# # app = Flask(__name__)
# # # if for some reason your conversation with Jabe gets weird, change the secret key

# # @app.route('/gradio', methods=['POST'])
# # def user():
# #  incoming_msg = request.values['Body']
# #  chat_log = session.get('chat_log')
# #  answer = ask(incoming_msg, chat_log)
# #  session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
# #  chat_log)
# # #  msg = MessagingResponse()
# #  msg.message(answer)
# #  return str(msg)
# # if __name__ == '__main__':
# #  app.run(debug=True)
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'asdffjfnfjnfvf'
# def chat_bot(question):
#     global chat_log
#     answer = ask(question, chat_log)
#     chat_log = append_interaction_to_chat_log(question, answer, chat_log)
#     return answer

# chat_log = session_prompt

# inputs = gr.inputs.Textbox(label="Query")
# outputs = gr.outputs.Textbox(label="Response")

# @app.route("/", methods=["POST","GET"])
# def chat():
#     query = request.form["input"]
#     response = chat_bot(query)
#     return jsonify({'output': response})

# title = "Munshi: AI Chatbot"
# description = "Chat with Munshi, an AI chatbot powered by OpenAI."
# examples = [["What is your name?"]]

# chat_interface = gr.Interface(fn=chat, inputs=inputs, outputs=outputs, title=title, description=description, examples=examples)
# if __name__ == '__main__':
#     print(chat_bot("What is my name?"))
#     chat_interface.launch()
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

    
    