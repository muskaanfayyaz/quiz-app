import streamlit as st  # for the web interface
import random  # for randomizing the questions
import time  # for the timer

# Title of the Application with Styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📝 Quiz Application</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #4CAF50;'>", unsafe_allow_html=True)

# Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
]

# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question

# Display the question with styling
st.markdown(f"<h3 style='color: #FF9800;'>{question['question']}</h3>", unsafe_allow_html=True)

# Create radio buttons for the options
selected_option = st.radio("**Choose your answer:**", question["options"], key="answer")

# Submit button to check the answer
if st.button("✅ Submit Answer"):
    if selected_option == question["answer"]:
        st.success("🎉 **Correct!** Well done!")
    else:
        st.error(f"❌ **Incorrect!** The correct answer is: **{question['answer']}**")

    # Wait for 3 seconds before showing the next question
    time.sleep(2)

    # Select a new random question
    st.session_state.current_question = random.choice(questions)

    # Rerun the app to display the next question
    st.rerun()
