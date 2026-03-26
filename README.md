# ApexTracker AI 🏅

**A Context-Aware Hybrid Training Agent built for the Gen AI Academy (APAC Edition).**

ApexTracker AI is an elite, intelligent sports science coach designed for athletes tackling complex, multi-disciplinary events. By combining real-time environmental data with a vector-searchable sports science database, it dynamically adjusts daily training loads, recovery protocols, and pacing strategies. 

If you are aiming for a specific goal—like a 1 hour 30-minute Hyrox finish—ApexTracker ensures your plan adapts to the physical world, substituting outdoor runs for indoor swimming if local heat or humidity becomes a barrier.

---

## 🏆 Hackathon Tracks Achieved

This project was built to address all three core tracks of the Gen AI Academy:

1. **Track 1: Build and Deploy AI Agent:** A fully autonomous conversational agent powered by Google Gemini 1.5 Flash, wrapped in a Streamlit frontend, and deployed via Docker to Google Cloud Run.
2. **Track 2: Connect AI Agents to Real-World Data:** Integrated a custom Model Context Protocol (MCP) tool utilizing WeatherAPI to fetch live, local environmental conditions (e.g., temperatures in Bengaluru) to inform training safety.
3. **Track 3: Build and Migrate faster with AI-Ready Databases:** Utilized Google Cloud AlloyDB for PostgreSQL with the `pgvector` extension to store, embed, and retrieve highly specific sports science recovery and pacing protocols.

---

## ⚙️ Tech Stack

* **Frontend:** Streamlit (Python)
* **AI Model:** Google Gemini 1.5 Flash (`google-generativeai`)
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
