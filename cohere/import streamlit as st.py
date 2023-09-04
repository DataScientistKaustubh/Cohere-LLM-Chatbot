import streamlit as st
import cohere

# Set your OpenAI API key here
co = cohere.Client('pjFvJkvoLCFvhpxC4yC6wpKFosqPYWu7IQxKptra')
# Add custom CSS to set the background image
st.markdown(
    
    <style>
    body {
        background-image: url('C:/cohere/Eviden/images/Eviden.png');
        background-size: cover;
        background-repeat: no-repeat;
    }
    </style>
    
    unsafe_allow_html=True,
)
# Create a title and user input textbox
st.title("Eviden personal assistant")
user_input = st.text_input("You:", "")

# Define a function to generate a response using ChatGPT
def generate_response(input_text):
    response = co.generate(
       model='command',
       prompt=input_text,
       max_tokens=300,
       temperature=0.9,
       k=0,
       stop_sequences=[],
       return_likelihoods='NONE')
    return response.generations[0].text

# Display the response
if user_input:
    response = generate_response(user_input)
    st.text("ChatGPT:")
    st.write(response)