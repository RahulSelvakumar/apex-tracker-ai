# ApexTracker AI 🏅

**A Context-Aware Hybrid Training Agent built for the Gen AI Academy (APAC Edition).**

**🔴 Live Demo:** [ApexTracker AI on Google Cloud Run](https://apextracker-1040501010782.us-central1.run.app/)

ApexTracker AI is an elite, intelligent sports science coach designed for athletes tackling complex, multi-disciplinary events. By combining real-time environmental data with a vector-searchable sports science database, it dynamically adjusts daily training loads, recovery protocols, and pacing strategies. 

---

## 🖥️ How to Use the Web App

Using the live agent is simple and requires just two inputs:

1. **Open the Live Demo:** Click the link above to access the Streamlit web interface.
2. **Enter Your Location:** In the "Training Location" box, type your current city (e.g., `Bengaluru`). The agent will use this to fetch live weather and humidity data via WeatherAPI.
3. **Log Your Status/Query:** In the text area, describe your planned workout, your specific race goals, or any fatigue/pain you are experiencing. (e.g., *"I have a 10km run today, but my shins hurt."*)
4. **Consult the AI:** Click the **"Consult AI Coach"** button.
5. **Review Your Plan:** The app will display the live data it gathered (Weather + Database protocols) and generate a custom, safe, and actionable daily training plan tailored to your exact situation.

---

## 🏆 Tracks

This project was built to address all three core tracks of the Gen AI Academy:

1. **Track 1: Build and Deploy AI Agent:** A fully autonomous conversational agent powered by Google Gemini 1.5 Flash, wrapped in a Streamlit frontend, and deployed via Docker to Google Cloud Run.
2. **Track 2: Connect AI Agents to Real-World Data:** Integrated a custom Model Context Protocol (MCP) tool utilizing WeatherAPI to fetch live, local environmental conditions to inform training safety.
3. **Track 3: Build and Migrate faster with AI-Ready Databases:** Utilized Google Cloud AlloyDB for PostgreSQL with the `pgvector` extension to store, embed, and retrieve highly specific sports science recovery and pacing protocols.

---

## 🎯 Example Prompts to Try

To see the full power of the agent, try copying and pasting these scenarios into the query box!

### Example 1: Acute Recovery & Injury Management (Tests Track 2 & 3)
* **Location:** `Bengaluru`
* **Your Query:** *"I'm experiencing heavy quad cramps and some shin pain after my last half marathon. I had a 10km run scheduled for today. What should I do?"*
* **What to Expect:** The AI will instruct you to immediately reduce running volume by 50%, suggest substituting the run with low-impact swimming to maintain your aerobic base, and provide specific hydration protocols from the AlloyDB database.

### Example 2: Event Pacing & Strategy (Tests Track 3)
* **Location:** `London`
* **Your Query:** *"I'm training for an upcoming Hyrox match on April 11. My goal is a 1 hour and 30-minute finish time. How should I approach my simulated workout today?"*
* **What to Expect:** The AI will pull the specific strategy from the vector database, advising you to maintain a strict Zone 3 heart rate on the 1km runs, bank your time on the sled push and row, and recover actively during the farmer's carry. 

### Example 3: Environmental Adaptation (Tests Track 2)
* **Location:** `Dubai`
* **Your Query:** *"I'm feeling good and want to do an outdoor threshold run today."*
* **What to Expect:** Because the MCP tool will detect extreme heat in Dubai, the AI will intercept the plan and dynamically suggest an indoor alternative, like a treadmill session or an indoor pool workout, to prevent heat exhaustion.

---

## ⚙️ Tech Stack

* **Frontend:** Streamlit (Python)
* **AI Model:** Google Gemini 2.5 Flash (`google-generativeai`)
* **Database:** Google Cloud AlloyDB (`psycopg2-binary`, `pgvector`)
* **External APIs:** WeatherAPI 
* **Deployment:** Docker, Google Cloud Run

---

## 📂 Project Structure

```text
apextracker/
│
├── app.py               # Core Streamlit application and Gemini agent logic
├── database_init.py     # Script to initialize AlloyDB and populate recovery protocols
├── weather_tool.py      # Tool to fetch real-time environmental data
├── requirements.txt     # Python dependencies
└── Dockerfile           # Containerization instructions for Cloud Run
