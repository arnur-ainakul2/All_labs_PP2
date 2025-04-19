import psycopg2

conn = psycopg2.connect(
    dbname="lab10",
    user="postgres",
    password="asdf1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS snake_game_scores (
        id SERIAL PRIMARY KEY,
        player_name VARCHAR(50),
        score INTEGER,
        level INTEGER
    );
""")

conn.commit()
cur.close()
conn.close()