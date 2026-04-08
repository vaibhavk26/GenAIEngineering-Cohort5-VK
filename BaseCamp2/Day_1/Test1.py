import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("GenAI Career Advisor")

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

responses = {}

st.write("Rate each statement:")
st.write("1 = Agree | 0 = Neutral | -1 = Disagree")

for i, s in enumerate(statements):
    responses[s["category"]] = st.radio(
        f"{i+1}. {s['text']}",
        options=[-1, 0, 1],
        horizontal=True
    )

if st.button("Submit"):

    scores = {}
    for cat, val in responses.items():
        scores[cat] = scores.get(cat, 0) + val

    prompt = f"""
You are a GenAI career advisor.

User scores:
{scores}

Tasks:
1. Identify top 3 strongest areas.
2. Suggest 3-5 career roles.
3. For each role include:
   - Area
   - Why it fits
   - 2 practical starting steps

Keep it concise and structured with bullet points.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    result = response.choices[0].message.content

    st.subheader("Your Results")
    st.write(result)