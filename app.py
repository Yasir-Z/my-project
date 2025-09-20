"""Flask application entry point."""

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def hello():
    """
    GET /
    Returns a simple greeting message as plain text.
    Response: "Hello from Flask!"
    """
    return "Hello from Flask!"


@app.route("/echo", methods=["POST"])
def echo():
    """
    POST /echo
    Accepts JSON data in the request body and echoes it back in the response.

    Request JSON example:
    {
        "key": "value"
    }

    Response JSON: Same as the request JSON.
    """
    data = request.json
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)


# trigger CI/CD
# trigger CI/CD 2nd time
