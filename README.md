# Hezane

Hezane is a Flask-based personal blog platform. It aims to provide a simple and customizable solution for publishing posts and managing content.

## Key Features

- User-friendly interface for creating and editing posts
- Responsive design with basic theming
- Simple authentication for managing posts
- Markdown support for writing content
- Lightweight architecture built on Flask

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd hezane
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```bash
   flask run
   ```
   The application will be available at `http://localhost:5000`.

## Folder Structure

```
hezane/
├── app/                # Application code
│   ├── __init__.py     # Flask app factory
│   ├── views.py        # Route definitions
│   └── models.py       # Database models
├── migrations/         # Database migrations
├── static/             # Static files (CSS, JS, images)
├── templates/          # Jinja2 templates
├── tests/              # Test suite
└── README.md           # Project documentation
```

Feel free to customize and extend the project to meet your specific needs.

