# 🚀 GitHub Profile Analyzer (Full Stack Project)

A full-stack Python application that fetches GitHub user data using the GitHub API, stores it in a PostgreSQL database, and displays it through a simple web interface.

---

## 📌 Features

- Fetch GitHub user data via username
- Store user data in PostgreSQL database
- Prevent duplicate entries
- Display stored users from database
- Simple web UI (HTML + JavaScript)
- REST API built with Flask
- Clean layered architecture (services, routes, DB)

---

## 🧠 How It Works

1. User enters a GitHub username in the UI
2. Frontend sends request to Flask API
3. Backend fetches data from GitHub API
4. Data is stored in PostgreSQL
5. Stored data can be retrieved via `/users`

---

## 🛠️ Tech Stack

- Python 🐍
- Flask (REST API)
- PostgreSQL (Database)
- psycopg2 (DB connector)
- HTML + JavaScript (Frontend)
- GitHub REST API

---

## 📁 Project Structure
