# Hezane Blog Platform

This repository contains a simple blog platform built with Flask. It allows you to create and view posts using a SQLite database.

## Setup

1. Create a virtual environment and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the database by running the application once:
   ```bash
   python -m blog.app
   ```
   The database `posts.db` will be created automatically.

4. Visit `http://localhost:5000` in your browser to view the blog.

## File Overview

- `blog/app.py` - main Flask application
- `blog/templates/` - HTML templates for the application
- `requirements.txt` - list of Python dependencies

Feel free to expand this project to build your portfolio!
