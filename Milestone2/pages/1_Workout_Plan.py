import streamlit as st
import os
import time
from huggingface_hub import InferenceClient
from prompt_builder import build_prompt

st.set_page_config(page_title="Your 5-Day Plan", page_icon="💎", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(10,10,20,0.7), rgba(10,10,20,0.7)),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
h1, h2, h3, h4, p { color: white !important; }
</style>
""", unsafe_allow_html=True)

def query_model(prompt):
    HF_TOKEN = os.getenv("HF_TOKEN")

    client = InferenceClient(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        token=HF_TOKEN
    )

    response = client.chat_completion(
        messages=[
            {"role": "system", "content": "You are a certified professional fitness trainer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.7
    )

    return response.choices[0].message.content

if "user_data" not in st.session_state:
    st.error("No user data found.")
    st.stop()

data = st.session_state.user_data

prompt, bmi, category = build_prompt(
    name=data["name"],
    gender="Not Specified",
    height=data["height"],
    weight=data["weight"],
    goal=data["goal"],
    fitness_level=data["level"],
    equipment=data["equipment"]
)

st.markdown("## 💎 Your 5-Day Personalized Workout Plan")
st.markdown(f"### 👤 {data['name']} | Age: {data['age']}")
st.markdown(f"### BMI: {bmi:.2f} ({category})")

progress = min(bmi/40,1.0)
bar = st.progress(0)
for i in range(int(progress*100)):
    time.sleep(0.01)
    bar.progress(i+1)

with st.spinner("Generating your elite workout plan..."):
    workout_plan = query_model(prompt)

formatted_plan = workout_plan.replace("\n", "<br>")

st.markdown(f"""
<div style="
    background: rgba(0,0,0,0.8);
    padding: 35px;
    border-radius: 20px;
    backdrop-filter: blur(25px);
    border: 2px solid rgba(255,0,200,0.6);
    box-shadow: 0 0 35px rgba(255,0,200,0.6);
    color: white;
    line-height: 1.8;
">
{formatted_plan}
</div>
""", unsafe_allow_html=True)

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")