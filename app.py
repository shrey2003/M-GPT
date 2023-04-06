import streamlit as st
from user import session_prompt,ask, append_interaction_to_chat_log
import speech_recognition as sr


st.set_page_config(page_title="Munshi: AI Chatbot", page_icon=":guardsman:", layout="wide")

def recognize_speech():
    # Create an instance of the Recognizer class
    r = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        
        # Ask the user for input
        print("Say something!")
        
        # Listen for the user's input
        audio = r.listen(source)
        
        try:
            # Recognize speech using Google Speech Recognition
            query = r.recognize_google(audio)
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            
    return ""


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

# Create a button to allow users to input text using speech
if st.button("Speak"):
    query = recognize_speech()
    st.text_input("Query", value=query)
else:
    # Otherwise, show a regular text input field
    query = st.text_input("Query")

if query:
    response = chat_bot(query)
    st.write(response)

    
    