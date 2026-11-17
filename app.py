"""Laboratory work No. 2: Hello World on Azure App Service (Flask)."""

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    """Main application page."""
    return render_template("index.html")


@app.get("/health")
def health():
    """A simple check that the Flask application is running."""
    return {"status": "ok", "application": "Lab2-IX32"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
