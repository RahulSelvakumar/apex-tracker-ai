import streamlit as st
import google.generativeai as genai
import os
from weather_tool import get_live_weather

# --- UI Config ---
st.set_page_config(page_title="ApexTracker AI", page_icon="🏅", layout="centered")

# --- Initialize Gemini ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('models/gemini-2.5-flash')
else:
    st.error("🚨 Missing Gemini API Key in environment variables.")

# --- Database Mock (Fallback for Hackathon Demo) ---
def get_recovery_context(query):
    """Simulates a vector search query to AlloyDB."""
    db_context = "No specific database matches found."
    query_lower = query.lower()
    
    if "shin" in query_lower or "cramp" in query_lower:
         db_context = "AlloyDB Protocol match: If experiencing shin pain or quad cramps, reduce running volume immediately. Substitute with low-impact swimming. Focus on hydration."
    elif "hyrox" in query_lower or "1h 30m" in query_lower:
         db_context = "AlloyDB Protocol match: For a 1h 30m finish, maintain Zone 3 HR on runs. Bank time on sleds, recover on carries."
         
    return db_context

# --- App Layout ---
st.title("ApexTracker AI 🏅")
st.markdown("**Context-Aware Hybrid Training Agent**")

st.divider()

user_city = st.text_input("Training Location:", value="Bengaluru")
user_input = st.text_area("Log your daily status:", 
                          placeholder="e.g., I'm aiming for a 1h 30m Hyrox finish. How should I pace today's run?")

if st.button("Consult AI Coach", type="primary"):
    if not user_input:
        st.warning("Please enter your training status.")
    else:
        with st.spinner("Analyzing environment and querying sports science database..."):
            
            # 1. Fetch Live Data (Track 2)
            live_weather = get_live_weather(user_city)
            
            # 2. Fetch Database Context (Track 3)
            db_context = get_recovery_context(user_input)
            
            # 3. Prompt Agent (Track 1)
            prompt = f"""
            You are ApexTracker, an elite AI coach for hybrid athletes.
            
            User Status: "{user_input}"
            
            REAL-WORLD CONTEXT (WeatherAPI): {live_weather}
            DATABASE CONTEXT (AlloyDB): {db_context}
            
            Task:
            1. Analyze the user's status against the real-world weather. If it's too hot (above 30°C), recommend indoor pool work or gym substitutions.
            2. Integrate the specific advice from the DATABASE CONTEXT.
            3. Provide a clear, actionable, and safe adjusted training plan. Format with bullet points.
            """
            
            try:
                response = model.generate_content(prompt)
                
                st.success("Plan Generated")
                st.markdown("### 📡 Data Gathered:")
                st.info(f"**Weather:** {live_weather}\n\n**DB Search:** {db_context}")
                
                st.markdown("### 🧠 Adjusted Protocol:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Generation failed: {e}")