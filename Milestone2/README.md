
⸻

💎 FitPlan AI – Personalized Fitness Plan Generator

🚀 Milestone 2: Core AI Model Integration

(LLM-Based Personalized Workout Generator)

⸻

📌 1. Project Overview

Milestone 2 enhances the FitPlan AI system by integrating a Large Language Model (LLM) to dynamically generate structured and personalized 5-day workout plans.

This milestone transforms the application from a static BMI calculator into a fully functional AI-powered fitness assistant.

🎯 Objectives
	•	Integrate a pre-trained LLM from Hugging Face
	•	Construct structured prompts using user fitness data
	•	Generate personalized 5-day workout plans dynamically
	•	Implement secure API authentication
	•	Deploy the upgraded AI system on Hugging Face Spaces

⸻

🤖 2. Features Implemented

🔥 AI Workout Plan Generator

The system now:
	•	Collects user fitness data from Milestone 1
	•	Dynamically constructs a structured AI prompt
	•	Sends the prompt to a pre-trained Hugging Face model
	•	Generates a complete 5-day personalized workout plan
	•	Displays the output in a styled UI workout card

⸻

📄 Multi-Page Application Architecture

The application now uses a structured multi-page flow:

🟢 Page 1 – User Profile Form
	•	Name input
	•	Age input (newly added)
	•	Height & Weight
	•	Fitness Goal selection
	•	Fitness Level selection
	•	Equipment selection

🔵 Page 2 – AI Workout Plan
	•	Displays BMI & BMI category
	•	Generates structured 5-day workout plan
	•	Styled output card with enhanced UI
	•	Navigation button to return to home

⸻

🧠 3. Model Integration

✅ Model Used

Qwen/Qwen2.5-7B-Instruct
(Instruction-tuned Large Language Model from Hugging Face)

⸻

🔧 Model Integration Workflow
	1.	Imported InferenceClient from huggingface_hub
	2.	Configured secure authentication using HF_TOKEN
	3.	Constructed chat-based structured messages
	4.	Generated AI responses using chat_completion()
	5.	Implemented robust error handling using try–except

Example Initialization

client = InferenceClient(
    model="Qwen/Qwen2.5-7B-Instruct",
    token=HF_TOKEN
)

📝 4. Prompt Engineering Strategy

The prompt dynamically includes:
	•	👤 Name
	•	🎂 Age
	•	📏 Height & Weight
	•	📊 Calculated BMI
	•	🏷 BMI Category
	•	🎯 Fitness Goal
	•	🏋️ Fitness Level
	•	🛠 Available Equipment

📌 System Instructions Ensure:
	•	Clearly divided Day 1 to Day 5
	•	Exercise names
	•	Sets & repetitions
	•	Rest intervals
	•	Intensity adjustments based on BMI
	•	Beginner safety considerations

This structured approach guarantees consistent, high-quality AI responses.

⸻

⚙️ 5. Error Handling & Validation

The application includes:
	•	✅ Secure HF_TOKEN validation
	•	✅ Model inference error handling
	•	✅ Graceful fallback messages
	•	✅ Required field validation
	•	✅ Session state management for multi-page flow

⸻

🧪 6. Testing Scenarios

The model was tested with diverse user profiles:

Scenario 1
	•	Beginner
	•	Weight Loss
	•	No Equipment

Scenario 2
	•	Intermediate
	•	Muscle Building
	•	Dumbbells & Bench

Scenario 3
	•	Advanced
	•	Strength Gain
	•	Full Equipment

Each scenario successfully generated structured and realistic 5-day workout plans.

⸻

🚀 7. Deployment

The upgraded AI-powered application is successfully deployed on Hugging Face Spaces.

🔗 Live Application

👉 https://huggingface.co/spaces/Karthik71212/fit_plan

✔ Deployment Verification
	•	Model loads successfully
	•	Authentication works via HF_TOKEN
	•	Multi-page navigation functioning
	•	AI plan generation working
	•	Clean UI rendering

⸻

🛠 8. Technologies Used
## 🛠 Technologies Used

| Technology            | Purpose                                   |
|-----------------------|-------------------------------------------|
| Python                | Core programming language                 |
| Streamlit             | Multi-page web application framework      |
| Hugging Face Hub      | LLM inference integration                 |
| Hugging Face Spaces   | Deployment platform                       |
| Git & GitHub          | Version control & repository hosting      |
| Prompt Engineering    | Structured AI response generation         |


```
FitPlan-AI/
└── Milestone2/
    ├── app.py
    ├── model_api.py
    ├── prompt_builder.py
    ├── requirements.txt
    ├── README.md
    ├── pages/
    │   └── 1_Workout_Plan.py
    └── screenshots/
```

⸻

✔ 10. Milestone Completion Status
	•	✔ LLM Integrated
	•	✔ Secure Authentication
	•	✔ Structured Prompt Design
	•	✔ 5-Day Workout Generation
	•	✔ Multi-Page Architecture
	•	✔ Successful Deployment
	•	✔ Error Handling Added

⸻

🎓 11. Internship Submission

Milestone 2 is now complete, transforming FitPlan AI into a fully functional AI-powered personalized fitness planner.