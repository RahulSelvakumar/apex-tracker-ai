import psycopg2
import os

# Replace with your actual AlloyDB credentials later
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASS", "password")
DB_NAME = os.environ.get("DB_NAME", "postgres")

def initialize_db():
    try:
        conn = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, dbname=DB_NAME)
        cur = conn.cursor()

        # Enable vector extension
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        
        # Create table for sports science protocols
        cur.execute("""
            CREATE TABLE IF NOT EXISTS recovery_protocols (
                id SERIAL PRIMARY KEY,
                issue_name VARCHAR(255),
                protocol_details TEXT,
                embedding vector(768)
            );
        """)

        cur.execute("TRUNCATE TABLE recovery_protocols;")

        # Insert highly specific hybrid-training data
        sample_data = [
            ("Quad cramps during half marathon", "Immediate: Stop and stretch. Hydrate with high-sodium electrolytes. Next 3 days: Substitute running with low-impact swimming to maintain aerobic base while repairing."),
            ("Shin pain from heavy running", "Reduce running volume by 50%. Ice shins for 15 mins post-workout. Switch cardio sessions to swimming to build endurance without impact."),
            ("Hyrox pacing strategy 1h 30m goal", "Maintain strict Zone 3 heart rate on all 1km runs. Bank time on the sled push and row. Recover actively during the farmer's carry.")
        ]

        for issue, protocol in sample_data:
            cur.execute(
                "INSERT INTO recovery_protocols (issue_name, protocol_details) VALUES (%s, %s)",
                (issue, protocol)
            )

        conn.commit()
        cur.close()
        conn.close()
        print("✅ AlloyDB initialized with recovery protocols.")

    except Exception as e:
        print(f"❌ DB connection skipped for local dev/hackathon fallback. Error: {e}")

if __name__ == "__main__":
    initialize_db()