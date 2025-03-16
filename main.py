import streamlit as st
import random

# Set up Streamlit Page
st.set_page_config(page_title="Quiz App", page_icon="📝", layout="centered")

st.title("📝 Quiz Application")

# Question Bank
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "correct_answer": "Islamabad"
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": ["Allama Iqbal", "Quaid e Azam", "Sir Syed Ahmad Khan", "Maulana Shaukat Ali"],
        "correct_answer": "Quaid e Azam"
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Pound", "Euro"],
        "correct_answer": "Rupee"
    },
    {
        "question": "Which is the largest city of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "correct_answer": "Karachi"
    },
    {
        "question": "What is the national language of Pakistan?",
        "options": ["Urdu", "English", "Punjabi", "Pashto"],
        "correct_answer": "Urdu"
    },
    {
        "question": "What is the national animal of Pakistan?",
        "options": ["Markhor", "Lion", "Tiger", "Deer"],
        "correct_answer": "Markhor"
    },
    {
        "question": "What are the colors of the national flag of Pakistan?",
        "options": ["Red and White", "Green and White", "Blue and White", "Yellow and White"],
        "correct_answer": "Green and White"
    },
    {
        "question": "What is the national flower of Pakistan?",
        "options": ["Rose", "Lily", "Tulip", "Jasmine"],
        "correct_answer": "Jasmine"
    },
    {
        "question": "What is the national bird of Pakistan?",
        "options": ["Chukar Partridge", "Peacock", "Pigeon", "Eagle"],
        "correct_answer": "Chukar Partridge"
    },
]

# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_option = None  # Store selected option separately

# Fetch Current Question
question = st.session_state.current_question

# Display Question
st.markdown(f"### {question['question']}")

# Display Options with Radio Buttons
selected_option = st.radio(
    "Select your answer:",
    question["options"],
    key="answer"
)

# Submit Button
if st.button("Submit"):
    if selected_option:
        if selected_option == question["correct_answer"]:
            st.success("✅ Correct answer!")
            if not st.session_state.answered:
                st.session_state.score += 1  # Increase score only once
        else:
            st.error(f"❌ Incorrect! The correct answer is: **{question['correct_answer']}**")
        st.session_state.answered = True
    else:
        st.warning("⚠️ Please select an answer before submitting.")

# Display Score
st.sidebar.title("📊 Scoreboard")
st.sidebar.write(f"**Score:** {st.session_state.score}")


# Rerun the app to display the next question    
st.rerun()
