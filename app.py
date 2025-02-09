import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

# Corrected text-generation pipeline
chatbot = pipeline("text-generation", model='distilgpt2')

def healthcare_chatbot(user_input):
    if "symptom" in user_input.lower():
        return "🩺 Please consult a doctor."
    elif "appointment" in user_input.lower():
        return "📅 Would you like to schedule an appointment with a doctor?"
    elif "medication" in user_input.lower():
        return "💊 It's important to take prescribed medications."
    else:
        response = chatbot(user_input, max_length=300, temperature=0.7, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title(" **Healthcare Chatbot** ")
    st.write("🤖 **I am here to assist you with healthcare-related queries.**")
    user_input = st.text_input("💬 **How can I assist you today?**")
    
    if st.button("🚀 Submit"):
        if user_input:
            st.write("👤 **User:** ", user_input)
            with st.spinner("⏳ **Processing your query, please wait...**"):
                response = healthcare_chatbot(user_input)
            st.success("🩺 **Healthcare Assistant:** " + response)
        else:
            st.warning("⚠️ Please enter a query!")

if __name__ == "__main__":
    main()
