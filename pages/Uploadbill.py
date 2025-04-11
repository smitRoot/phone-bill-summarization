import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# Configure your Gemini API key
genai.configure(api_key="")  # Replace with your actual API key
model = genai.GenerativeModel('gemini-1.5-flash')  # Use 'gemini-pro' for text-only

# Check if user is authenticated
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("You must log in first!")
    st.stop()
else:       
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"Welcome, {st.session_state.get('username', '')}! 👋")    
    with col2:
        if st.button("Logout"):
            st.session_state.clear()
            st.rerun()

# Title and upload section
st.title("Bill Buddy")
st.subheader("Upload your Bill PDF")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

if st.button("Submit"):
    if uploaded_file is not None:
        st.success("File uploaded successfully!")

        # Extract text from the PDF
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""  # Handle potential NoneType return

        # Prepare the initial prompt
        prompt = """
        Based on the existing usage from the provided bill, 
        what do you think is the best plan? 
        Or is there any cheaper option available in the market?
        
        Can you analyze my bill and identify any areas where I might be able to reduce costs?
        
        Are there any discounts available to me that I'm not currently taking advantage of?

        i found some plan please check below 

        plans = [
    # T-Mobile Plans
    {"provider": "T-Mobile", "name": "Essentials Saver", "cost_per_line": [None, 50, 70, 100, 120], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "T-Mobile", "name": "Go5G Next", "cost_per_line": [None, 95, 145, 195, 245], "premium_data": float("inf"), "apple_tv_netflix": True, "upgrade_ready": True, "hulu_included": False},
    {"provider": "T-Mobile", "name": "Go5G Plus", "cost_per_line": [None, 105, 155, 190, 240], "premium_data": float("inf"), "apple_tv_netflix": True, "upgrade_ready": True, "hulu_included": False},
    {"provider": "T-Mobile", "name": "Essentials", "cost_per_line": [None, 65, 105, 135, 160], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "T-Mobile", "name": "Go5G", "cost_per_line": [None, 80, 120, 160, 180], "premium_data": 100, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},

    # Verizon Plans
    {"provider": "Verizon", "name": "Welcome", "cost_per_line": [None, 70, 95, 125, 160], "premium_data": 0, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "Verizon", "name": "5G Start", "cost_per_line": [None, 75, 100, 130, 160], "premium_data": 0, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "Verizon", "name": "5G Do More", "cost_per_line": [None, 85, 120, 155, 180], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "Verizon", "name": "5G Play More", "cost_per_line": [None, 90, 130, 160, 190], "premium_data": 50, "apple_tv_netflix": True, "upgrade_ready": False, "hulu_included": True},
    {"provider": "Verizon", "name": "5G Get More", "cost_per_line": [None, 100, 130, 170, 200], "premium_data": 100, "apple_tv_netflix": True, "upgrade_ready": False, "hulu_included": True},

    # AT&T Plans
    {"provider": "AT&T", "name": "Unlimited Starter", "cost_per_line": [None, 70, 95, 120, 150], "premium_data": 0, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "AT&T", "name": "Unlimited Extra", "cost_per_line": [None, 80, 105, 140, 175], "premium_data": 50, "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False},
    {"provider": "AT&T", "name": "Unlimited Premium", "cost_per_line": [None, 90, 120, 150, 190], "premium_data": float("inf"), "apple_tv_netflix": False, "upgrade_ready": False, "hulu_included": False}
]


if you found suitable plan from above please suggest me tahat first please and let me know how much money i can save i will explore website further .
        """

        # Gemini API call (using text from PDF)
        try:
            response = model.generate_content([prompt, text])
            st.subheader("Gemini's Analysis:")
            st.write(response.text)
            # Store response in conversation history
            st.session_state.conversation_history.append(f"Gemini's Analysis: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload a PDF file before submitting.")

# Input for follow-up questions
user_query = st.text_input("Ask a follow-up question or query:", "")

if user_query:
    # Append the query to conversation history
    st.session_state.conversation_history.append(f"User: {user_query}")

    # Prepare the prompt with conversation context
    full_conversation = "\n".join(st.session_state.conversation_history) + "\nAnswer the question above."
    
    try:
        # Gemini API call to generate a response to the user's follow-up query
        response = model.generate_content([full_conversation])
        st.subheader("Gemini's Follow-up Response:")
        st.write(response.text)
        # Store the follow-up response in conversation history
        st.session_state.conversation_history.append(f"Gemini's Follow-up Response: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
