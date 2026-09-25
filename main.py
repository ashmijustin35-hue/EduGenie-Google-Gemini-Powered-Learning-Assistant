import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(
    page_title="EduGenie - AI Learning Assistant",
    page_icon="🎓",
    layout="wide"
)

API_KEY = os.getenv("GEMINI_API_KEY")

st.title("🎓 EduGenie")
st.subheader("Google Gemini Powered Learning Assistant")
st.write("Ask questions, simplify topics, generate study notes, and create quizzes.")

if not API_KEY or API_KEY == "your_gemini_api_key_here":
    st.warning("Please add your Gemini API key to the .env file.")
    st.code("GEMINI_API_KEY=your_gemini_api_key_here")
    st.stop()

client = genai.Client(api_key=API_KEY)

with st.sidebar:
    st.header("📚 Learning Tools")
    mode = st.selectbox(
        "Choose a mode",
        [
            "Ask a Question",
            "Explain Simply",
            "Create Study Notes",
            "Create Quiz",
            "Summarize Text"
        ]
    )
    st.divider()
    st.caption("EduGenie uses Google Gemini to generate learning assistance.")

topic = st.text_area(
    "Enter your question or topic",
    placeholder="Example: Explain photosynthesis in simple words."
)

if mode == "Create Quiz":
    number = st.slider("Number of questions", 3, 15, 5)
else:
    number = 5

if st.button("✨ Generate", type="primary"):
    if not topic.strip():
        st.error("Please enter a question or topic.")
    else:
        if mode == "Ask a Question":
            prompt = f"""
You are EduGenie, a friendly learning assistant.
Answer the student's question clearly and accurately.

Question:
{topic}

Use simple language and give examples when useful.
"""
        elif mode == "Explain Simply":
            prompt = f"""
Explain the following topic to a college student in very simple language.

Topic:
{topic}

Include:
1. Simple definition
2. Main idea
3. Easy example
4. Short recap
"""
        elif mode == "Create Study Notes":
            prompt = f"""
Create clear study notes for the following topic.

Topic:
{topic}

Include important definitions, concepts, examples, and a short revision summary.
Use headings and bullet points.
"""
        elif mode == "Create Quiz":
            prompt = f"""
Create {number} multiple-choice questions for a student studying:
{topic}

For each question provide four options (A-D), the correct answer, and a one-sentence explanation.
Do not make the questions ambiguous.
"""
        else:
            prompt = f"""
Summarize the following text for a student.

Text:
{topic}

Give:
- Key points
- Important terms
- A short final summary
"""

        with st.spinner("EduGenie is thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                st.markdown("### 📖 EduGenie Response")
                st.markdown(response.text)
            except Exception as e:
                st.error("Something went wrong while contacting Gemini.")
                st.code(str(e))

st.divider()
st.caption("💡 Tip: Ask EduGenie to explain a topic at your level, create revision notes, or generate a practice quiz.")
