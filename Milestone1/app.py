import streamlit as st
import time

# --- 1. App Configuration & Styling ---
def setup_page():
    st.set_page_config(
        page_title="FitPlan AI",
        page_icon="💪",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # --- CSS FIXES ---
    # 1. Removed fixed light background color.
    # 2. Used rgba(255,255,255,0.1) for a glass-morphism effect in dark mode.
    # 3. Added specific border styling for better definition.
    st.markdown("""
        <style>
        .main {
            padding-top: 2rem;
        }
        /* Metric Box Styling */
        div[data-testid="stMetricValue"] {
            font-size: 2rem;
        }
        div[data-testid="stMetric"] {
            background-color: rgba(255, 255, 255, 0.1); /* Semi-transparent dark bg */
            border: 1px solid rgba(255, 255, 255, 0.2); /* Subtle border */
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Slight shadow for depth */
        }
        /* Remove default container padding to fit boxes better */
        div[data-testid="stMetricLabel"] {
            font-weight: bold;
            color: rgba(255, 255, 255, 0.8); /* Slightly dimmed white for labels */
        }
        div[data-testid="stExpander"] div[role="button"] p {
            font-size: 1.1rem;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. Logic & Helper Functions ---
def calculate_bmi(weight_kg, height_cm):
    """
    Calculates BMI, returns score, category, and color code.
    """
    if height_cm <= 0 or weight_kg <= 0:
        return 0, "N/A", "#ecf0f1"
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)
    
    if bmi < 18.5:
        return bmi, "Underweight", "#3498db" # Blue
    elif 18.5 <= bmi < 24.9:
        return bmi, "Normal Weight", "#2ecc71" # Green
    elif 25 <= bmi < 29.9:
        return bmi, "Overweight", "#f1c40f" # Yellow/Orange
    else:
        return bmi, "Obese", "#e74c3c" # Red

# --- 3. Sidebar Module (Input Layer) ---
def sidebar_interface():
    with st.sidebar:
        st.header("💪 FitPlan AI")
        st.caption("Personalized Workout Generator")
        st.divider()
        
        with st.form("user_input_form"):
            st.subheader("1. Profile Details")
            c1, c2 = st.columns(2)
            with c1:
                name = st.text_input("First Name", placeholder="Alex")
            with c2:
                age = st.number_input("Age", 10, 100, 25)
            
            c3, c4 = st.columns(2)
            with c3:
                height = st.number_input("Height (cm)", 100.0, 250.0, 170.0)
            with c4:
                weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
                
            st.subheader("2. Fitness Goals")
            goal = st.selectbox(
                "Primary Goal", 
                ["Build Muscle", "Weight Loss", "Strength Gain", "Endurance", "Flexibility"]
            )
            level = st.select_slider(
                "Experience Level", 
                options=["Beginner", "Intermediate", "Advanced"]
            )
            
            st.subheader("3. Schedule & Equipment")
            days_per_week = st.slider("Workout Days / Week", 1, 7, 3)
            duration = st.slider("Minutes / Session", 15, 120, 45)
            
            equipment = st.multiselect(
                "Available Equipment",
                ["No Equipment", "Dumbbells", "Resistance Bands", "Yoga Mat", "Pull-up Bar", "Gym Machines"],
                default=["No Equipment", "Dumbbells"]
            )
            
            st.markdown("---")
            submit = st.form_submit_button("🚀 Generate Profile", type="primary")
            
        return submit, name, age, height, weight, goal, level, days_per_week, duration, equipment

# --- 4. Main Dashboard Views ---
def show_dashboard(name, age, height, weight, bmi, bmi_category, bmi_color, goal, level, equipment):
    st.title(f"Welcome back, {name}!")
    st.markdown("Here is your current fitness snapshot based on the data provided.")

    # Top Row: Key Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("BMI Score", bmi, delta_color="off")
    c2.metric("Current Weight", f"{weight} kg")
    c3.metric("Height", f"{height/100} m")
    c4.metric("Age", f"{age} yrs")

    # BMI Visualization Card
    st.markdown("### Health Analysis")
    with st.container():
        # Visual Progress Bar for BMI
        st.write(f"**Category:** {bmi_category}")
        # Normalize BMI for progress bar (0 to 40 scale roughly)
        progress_val = min(max((bmi / 40), 0.0), 1.0)
        st.progress(progress_val)
        
        # Color-coded feedback box
        st.markdown(f"""
            <div style="padding: 15px; border-radius: 8px; background-color: {bmi_color}20; border-left: 5px solid {bmi_color};">
                <p style="margin: 0; color: white;">Based on your BMI of <strong>{bmi}</strong>, you are in the <strong>{bmi_category}</strong> range.</p>
            </div>
        """, unsafe_allow_html=True)
        
    # Profile Summary
    st.markdown("### 📋 Configuration Summary")
    with st.expander("View Active Configuration", expanded=True):
        sc1, sc2 = st.columns(2)
        with sc1:
            st.write(f"**Goal:** {goal}")
            st.write(f"**Level:** {level}")
        with sc2:
            st.write(f"**Equipment:** {', '.join(equipment) if equipment else 'Bodyweight only'}")

def show_plan_placeholder(goal, days, duration):
    st.title("🗓️ Your AI Workout Plan")
    st.info("The AI Generation Module is currently under development (Milestone 2).")
    
    st.markdown(f"""
    ### Projected Plan Structure
    Based on your inputs, the AI will generate a **{days}-day split** focusing on **{goal}**.
    Each session will last approximately **{duration} minutes**.
    
    #### Preview (Static Mockup):
    """)
    
    mock_data = {
        "Day": ["Day 1", "Day 2", "Day 3"],
        "Focus": ["Upper Body Strength", "Lower Body Power", "Active Recovery / Cardio"],
        "Exercises": ["Bench Press, Rows, Overhead Press", "Squats, Lunges, Calf Raises", "Jogging, Stretching, Yoga"]
    }
    st.table(mock_data)

# --- 5. Main Execution Flow ---
def main():
    setup_page()
    
    if "form_submitted" not in st.session_state:
        st.session_state.form_submitted = False
    
    submit, name, age, height, weight, goal, level, days, duration, equipment = sidebar_interface()
    
    if submit:
        st.session_state.form_submitted = True
        st.session_state.user_data = {
            "name": name, "age": age, "height": height, "weight": weight,
            "goal": goal, "level": level, "days": days, "duration": duration,
            "equipment": equipment
        }

    if st.session_state.form_submitted:
        data = st.session_state.user_data
        
        bmi, category, color = calculate_bmi(data['weight'], data['height'])
        
        tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📅 Workout Plan", "⚙️ Settings"])
        
        with tab1:
            show_dashboard(
                data['name'], data['age'], data['height'], data['weight'], 
                bmi, category, color, data['goal'], data['level'], data['equipment']
            )
        
        with tab2:
            show_plan_placeholder(data['goal'], data['days'], data['duration'])
            
        with tab3:
            st.write("User settings and account management will appear here.")
            
    else:
        st.title("💪 Welcome to FitPlan AI")
        st.markdown("""
        ### Get Started
        Please fill out the **User Profile** form in the sidebar to generate your personalized dashboard.
        """)

if __name__ == "__main__":
    main()