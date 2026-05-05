import requests
from app.db import get_connection


# -----------------------
# FETCH + STORE USER
# -----------------------
def fetch_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "User not found"}, 404

    data = response.json()
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM users WHERE username=%s", (data["login"],))
    existing = cursor.fetchone()

    if existing:
        conn.close()
        return {"message": "User already exists"}, 200

    cursor.execute(
        "INSERT INTO users (username, public_repos, followers) VALUES (%s, %s, %s)",
        (data["login"], data["public_repos"], data["followers"])
    )

    conn.commit()
    conn.close()

    return {
        "username": data["login"],
        "repos": data["public_repos"],
        "followers": data["followers"]
    }, 201

# -----------------------
# GET ALL USERS
# -----------------------
def get_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "id": r[0],
            "username": r[1],
            "repos": r[2],
            "followers": r[3]
        } for r in rows
    ]