import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="FitPlan AI Elite", page_icon="💎", layout="wide")

# =============================
# FULL PREMIUM STYLING
# =============================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

/* Background */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(10,10,20,0.75), rgba(10,10,20,0.75)),
        url("https://images.unsplash.com/photo-1599058917765-a780eda07a3e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Center container */
.block-container {
    max-width: 950px;
    margin: auto;
    padding-top: 60px;
}

/* Text */
h1, h2, h3, h4, p, label {
    color: white !important;
}

/* =============================
   DARK MODERN INPUTS
============================= */

/* Text & Number input container */
div[data-baseweb="input"] {
    background-color: rgba(25, 25, 35, 0.95) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    backdrop-filter: blur(12px);
    padding: 6px !important;
    transition: all 0.3s ease !important;
}

/* Remove inner white */
div[data-baseweb="input"] > div {
    background: transparent !important;
}

/* Actual input */
div[data-baseweb="input"] input {
    background: transparent !important;
    color: #e6e6e6 !important;
    border: none !important;
    box-shadow: none !important;
}

/* Number step buttons */
div[data-baseweb="input"] button {
    background: transparent !important;
    color: #00f0ff !important;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background-color: rgba(25, 25, 35, 0.95) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: #e6e6e6 !important;
}

/* Multiselect */
.stMultiSelect > div > div {
    background-color: rgba(25, 25, 35, 0.95) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

/* Hover glow */
div[data-baseweb="input"]:hover,
.stSelectbox div[data-baseweb="select"]:hover,
.stMultiSelect > div > div:hover {
    border: 1px solid rgba(255,0,200,0.7) !important;
    box-shadow: 0 0 12px rgba(255,0,200,0.4) !important;
}

/* =============================
   NEON BUTTON
============================= */

.stButton > button {
    background: rgba(255,255,255,0.12) !important;
    border-radius: 40px !important;
    padding: 14px 50px !important;
    border: 2px solid rgba(255,255,255,0.4) !important;
    color: white !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #ff00cc, #7928ca, #00f0ff) !important;
    background-size: 300% 300% !important;
    animation: neonMove 4s ease infinite !important;
    box-shadow:
        0 0 20px #ff00cc,
        0 0 40px #7928ca,
        0 0 60px #00f0ff,
        0 0 80px #ff00cc !important;
    transform: translateY(-4px) scale(1.08) !important;
}

@keyframes neonMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

</style>
""", unsafe_allow_html=True)

# =============================
# HERO
# =============================
st.markdown("<h1 style='text-align:center;'>💎 FitPlan AI Elite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Train Smart. Perform Elite.</p>", unsafe_allow_html=True)

# =============================
# FEATURE SECTION
# =============================
components.html("""
<div style="display:flex;align-items:center;justify-content:center;gap:40px;margin:80px 0;">
    <div style="width:230px;border-radius:25px;overflow:hidden;">
        <img src="https://images.unsplash.com/photo-1594737625785-a6cbdabd333c?auto=format&fit=crop&w=600&q=80"
             style="width:100%;border-radius:25px;">
    </div>

    <div style="
        max-width:650px;
        padding:40px;
        border-radius:25px;
        background:rgba(255,255,255,0.05);
        backdrop-filter:blur(30px);
        border:2px solid rgba(255,0,200,0.7);
        box-shadow:0 0 40px rgba(255,0,200,0.6);
        text-align:center;
        color:white;
    ">
        <h3>🔥 Next-Gen AI Fitness Intelligence</h3>
        <p>Smart BMI • AI Plans • Optimized Progression</p>
    </div>

    <div style="width:230px;border-radius:25px;overflow:hidden;">
        <img src="https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?auto=format&fit=crop&w=600&q=80"
             style="width:100%;border-radius:25px;">
    </div>
</div>
""", height=420)

# =============================
# FORM
# =============================
name = st.text_input("Full Name")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=15, max_value=60, step=1)

with col2:
    height_cm = st.number_input("Height (cm)", min_value=0, step=1)

with col3:
    weight_kg = st.number_input("Weight (kg)", min_value=0)

goal = st.selectbox("Goal",
    ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
)

level = st.selectbox("Level",
    ["Beginner", "Intermediate", "Advanced"]
)

equipment = st.multiselect("Equipment",
    ["Dumbbells", "Resistance Band", "Yoga Mat", "Bench", "Pullup Bar"]
)

generate = st.button("Generate Elite Plan 🚀")

# =============================
# REDIRECT TO WORKOUT PAGE
# =============================
if generate:
    if name and age and height_cm > 0 and weight_kg > 0:

        st.session_state.user_data = {
            "name": name,
            "age": age,
            "height": height_cm,
            "weight": weight_kg,
            "goal": goal,
            "level": level,
            "equipment": equipment
        }

        st.switch_page("pages/1_Workout_Plan.py")

    else:
        st.error("Please fill all required fields.")