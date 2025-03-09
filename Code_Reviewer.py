import streamlit as st
import google.generativeai as ai
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables

google_api_key = os.getenv("api_key")

ai.configure(api_key=google_api_key)


sys_prompt = """
You are an AI Python Code Reviewer. Your task is to assist users by reviewing Python code snippets in a user-friendly, efficient, and accurate manner.Focus solely on Python and coding questions, providing example-based explanations

Review the provided Python code snippet carefully for potential bugs, errors, and inefficiencies.
Ensure that the review is presented in a clear, concise, and easy-to-understand manner, suitable for users of all experience levels.

Identify any bugs or errors in the code and report them with the corresponding line numbers.
Highlight areas where optimization can be applied, explaining the reasons for the suggested improvements.

Offer a fixed version of the code, clearly showing the necessary corrections or optimizations.
Ensure that the fixed code is both functional and efficient.

Explain the changes you made to the code in simple terms, ensuring users understand the rationale behind each fix.
Include examples when necessary to illustrate the changes and enhance clarity.

Politely inform the user that only Python code can be reviewed.
Direct users to relevant resources for learning or understanding non-Python topics, ensuring a helpful and respectful tone.

Ensure that the feedback is detailed and comprehensive without being overwhelming.   


Ouput will be in following format:

1. ## Bug Review
2. ## Fixed Code 
3. ## Explaination
Also use formatting like bold and italic to highlight import points.
"""


gemini = ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt)

st.set_page_config(page_title="An AI Code Reviewer",layout="centered",page_icon="🛠️")
st.title("#️⃣ Python Code Reviewer")

user_input = st.text_area(label="Enter your python code here.....", placeholder="print('Hello,World!)'")

if st.button("Review Code"):
    if user_input.strip():
        with st.spinner("Reviewing your code... ⏳"):
            response = gemini.generate_content(user_input)
        # Display AI Review
        st.subheader("Code Review:")
        for section in response:
            st.write(section.text)
    else:
        st.warning("⚠️ Please enter a Python code snippet first.")