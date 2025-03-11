"""Flask application for Gemini Chatbot."""

from flask import Flask, render_template, request, jsonify
from src.chatbot import Chatbot

app = Flask(__name__)
chatbot_instance = Chatbot()


@app.route("/")
def index():
    """Render the main chat interface."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """Handle incoming chat messages and return a chatbot response."""
    message = request.get_json().get("message")
    if not message:
        return jsonify({"error": "Message is required"}), 400

    response = chatbot_instance.process_message(message)
    return jsonify({"response": response})


@app.route("/clear", methods=["POST"])
def clear():
    """Clear the chat history."""
    chatbot_instance.clear_history()
    return jsonify({"message": "Chat history cleared"})


if __name__ == "__main__":
    app.run(debug=True)
