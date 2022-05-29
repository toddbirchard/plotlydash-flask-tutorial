"""Application entry point."""
from plotly_flask_tutorial import init_app

app = init_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
