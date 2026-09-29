from flask import Flask, render_template, request, jsonify

from agent import agent

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    question = request.form.get("question")

    if not question:
        return jsonify({
            "response": "Please enter a question."
        }), 400

    try:

        response = agent.run(question)

        answer = response.content

        return jsonify({
            "response": answer
        }), 200

    except Exception as e:

        print("Agent Error:", e)

        return jsonify({
            "response": "Sorry, something went wrong while processing your request."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
