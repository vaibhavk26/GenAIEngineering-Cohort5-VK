import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page configuration for modern look
st.set_page_config(
    page_title="GenAI Career Advisor",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Custom CSS for minimalist styling
st.markdown("""
<style>
body {
    background-color: #f8f9fa;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #333;
}
.stTitle {
    text-align: center;
    color: #2c3e50;
    font-weight: 300;
}
.stSubheader {
    color: #34495e;
    font-weight: 400;
}
.stButton>button {
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 16px;
    transition: background-color 0.3s;
}
.stButton>button:hover {
    background-color: #2980b9;
}
.stProgress > div > div > div {
    background-color: #3498db;
}
.stRadio > div {
    display: flex;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

st.title("GenAI Career Advisor")

# Main container for centered layout
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        statements = [
            {"category": "Data", "text": "I enjoy exploring large datasets to find meaningful patterns."},
            {"category": "Data Analysis", "text": "I like using statistical tools to turn raw data into insights."},
            {"category": "ML Ops", "text": "Automating model deployment and monitoring excites me."},
            {"category": "Building Applications", "text": "Building end-to-end software products motivates me."},
            {"category": "Agents", "text": "Designing autonomous AI agents appeals to me."},
            {"category": "Chatbots", "text": "Crafting chatbots that hold natural conversations is rewarding."},
            {"category": "Evals & Testing", "text": "I enjoy stress-testing AI models."},
            {"category": "Cost Control", "text": "Optimizing compute cost in ML workflows motivates me."},
            {"category": "Fine-Tuning", "text": "Adapting pre-trained models interests me."},
            {"category": "Guardrails", "text": "Ensuring AI safety and ethics matters to me."}
                ]

        # Initialize session state
        if "step" not in st.session_state:
            st.session_state.step = 0

        if "responses" not in st.session_state:
            st.session_state.responses = {}

        # Progress bar
        progress = st.session_state.step / len(statements)
        st.progress(progress)

        # If questions still remain
        if st.session_state.step < len(statements):

            current_q = statements[st.session_state.step]

            st.subheader(f"Question {st.session_state.step + 1} / {len(statements)}")
            st.write(current_q["text"])

            # Get previously saved answer if exists
            previous_answer = st.session_state.responses.get(current_q["category"], 0)

            answer = st.radio(
                "Your answer:",
                [-1, 0, 1],
                format_func=lambda x: {1: "Agree", 0: "Neutral", -1: "Disagree"}[x],
                index=[-1, 0, 1].index(previous_answer),
                key=f"q_{st.session_state.step}"
            )

            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Back", use_container_width=True):
                    if st.session_state.step > 0:
                        st.session_state.step -= 1
                        st.rerun()
            
            with col2:
                if st.button("Next", use_container_width=True):
                    st.session_state.responses[current_q["category"]] = answer
                    st.session_state.step += 1
                    st.rerun()

        # After all questions → show result
        else:
            st.success("All questions completed!")

            # Aggregate scores
            scores = {}
            for cat, val in st.session_state.responses.items():
                scores[cat] = scores.get(cat, 0) + val

            st.markdown("### 📊 Your Scores")
            
            # Display scores in a user-friendly format
            score_text = "\n\n".join([
                f"**{category}**: {'🟢 Strong Interest' if score > 0 else '🔵 Neutral' if score == 0 else '⚪ Less Interest'} (Score: {score:+d})"
                for category, score in sorted(scores.items(), key=lambda x: x[1], reverse=True)
            ])
            st.markdown(score_text)

            prompt = f"""
You are a GenAI career advisor. Respond in a friendly, easy-to-read format.

User scores:
{scores}

Tasks:
1. Identify top 3 strongest areas.
2. Suggest 3-5 career roles.
3. For each role include:
   - Area
   - Why it fits
   - 2 practical starting steps

Important: Format your response as plain text with clear headings and bullet points. Do NOT use JSON or any code format. Use emojis to make it engaging. Make it conversational and encouraging.
"""

            if st.button("Get Career Suggestions"):
                with st.spinner("Generating your career suggestions..."):
                    try:
                        response = client.chat.completions.create(
                            model="openai/gpt-oss-120b",
                            messages=[{"role": "user", "content": prompt}],
                            temperature=0.7
                        )

                        result = response.choices[0].message.content

                        st.subheader("🎯 Your Career Recommendations")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
                        st.write("Please check your API key and try again.")

            # Restart option
            if st.button("Start Over"):
                st.session_state.step = 0
                st.session_state.responses = {}