import sqlite3

def create_db():
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT,
            content TEXT,
            scheduled_time TEXT,
            posted INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_post(platform, content, scheduled_time):
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (platform, content, scheduled_time) VALUES (?, ?, ?)",
                   (platform, content, scheduled_time))
    conn.commit()
    conn.close()

def get_scheduled_posts():
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts WHERE posted = 0")
    posts = cursor.fetchall()
    conn.close()
    return [{"id": p[0], "platform": p[1], "content": p[2], "scheduled_time": p[3]} for p in posts]

create_db()
