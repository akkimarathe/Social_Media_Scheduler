from flask import Flask, request, jsonify
import sqlite3
from database import add_post, get_scheduled_posts
from scheduler import start_scheduler

app = Flask(__name__)

@app.route('/schedule', methods=['POST'])
def schedule_post():
    data = request.json
    platform = data.get("platform")
    content = data.get("content")
    scheduled_time = data.get("scheduled_time")

    if not platform or not content or not scheduled_time:
        return jsonify({"error": "Missing fields"}), 400

    add_post(platform, content, scheduled_time)
    return jsonify({"message": "Post scheduled successfully"}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = get_scheduled_posts()
    return jsonify(posts)

if __name__ == '__main__':
    start_scheduler()
    app.run(debug=True)

