from flask import Flask, request, jsonify
from flask_cors import CORS

from answer_engine import AnswerEngine

app = Flask(__name__)
CORS(app)

KDF_PATH = "../kdf/software_product"

engine = AnswerEngine(kdf_path=KDF_PATH)


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "Query is required"}), 400

    try:
        result = engine.get_answer(query)
        return jsonify(result)
    except Exception as e:
        return jsonify({
            "fallback": True,
            "response": "Internal processing error",
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(port=5001, debug=True)