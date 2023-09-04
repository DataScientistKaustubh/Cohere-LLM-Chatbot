import streamlit as st
import cohere
from PIL import  Image
img = Image.open('logo.jpg')
st.set_page_config(page_title= 'Eviden Assistant',page_icon=img)

# Set your Cohere API key here
co = cohere.Client('pjFvJkvoLCFvhpxC4yC6wpKFosqPYWu7IQxKptra')

# Create a title and user input textbox
#st.title("Eviden personal assistant")


# Add a title and logo image from a URL
logo_url = "https://bmtjeseh3bsw.objectstorage.ap-mumbai-1.oci.customer-oci.com/n/bmtjeseh3bsw/b/bucket-20230803-1207/o/Eviden%20ImagesMicrosoftTeams-image%20(5).png"  # Replace with your logo URL
#st.image(logo_url, width=700)

st.markdown(
    f"""
    <style>
        .reportview-container .main .block-container{{
            max-width: 100%;
            padding-top: 0rem;
            padding-right: 1rem;
            padding-left: 1rem;
            padding-bottom: 2rem;
        }}
        .reportview-container .main {{
            padding: 0rem;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


# Create a sidebar
with st.sidebar:
    st.markdown("Welcome!!!")
    
    # Insert an image using HTML
    st.markdown('<img src="https://bmtjeseh3bsw.objectstorage.ap-mumbai-1.oci.customer-oci.com/n/bmtjeseh3bsw/b/bucket-20230803-1207/o/Eviden%20ImagesMicrosoftTeams-image%20(5).png" alt="Sidebar Image" width="150">', unsafe_allow_html=True)
    
    user_name = st.text_input("Tenancy_name", "atossyntelcloud")
    language = st.selectbox("Roles", ["Developer", "Architect", "Management People,Functional,Others"])

#Taking User Input
user_input = st.chat_input("Say something")
# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define a function to generate a response using Cohere
def generate_response(input_text):
    response = co.generate(
        model='command',
        prompt=input_text,
        max_tokens=500,
        temperature=0.7,
        k=50,
        stop_sequences=[],
        return_likelihoods='NONE')
    return response.generations[0].text

# Handle user input and assistant response
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = generate_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display the entire chat conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
