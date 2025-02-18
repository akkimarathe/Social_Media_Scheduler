import time
import threading
import schedule
import sqlite3
from api_config import post_to_twitter, post_to_facebook, post_to_instagram

def check_scheduled_posts():
    while True:
        conn = sqlite3.connect("scheduler.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, platform, content, scheduled_time FROM posts WHERE posted = 0")
        posts = cursor.fetchall()
        conn.close()

        for post in posts:
            post_id, platform, content, scheduled_time = post
            current_time = time.strftime("%Y-%m-%d %H:%M")

            if scheduled_time == current_time:
                success = False
                if platform == "Twitter":
                    success = post_to_twitter(content)
                elif platform == "Facebook":
                    success = post_to_facebook(content)
                elif platform == "Instagram":
                    success = post_to_instagram(content)

                if success:
                    conn = sqlite3.connect("scheduler.db")
                    cursor = conn.cursor()
                    cursor.execute("UPDATE posts SET posted = 1 WHERE id = ?", (post_id,))
                    conn.commit()
                    conn.close()

        time.sleep(60)

def start_scheduler():
    thread = threading.Thread(target=check_scheduled_posts, daemon=True)
    thread.start()
