from flask import Flask, request, jsonify
from model import ModelClassifier
import db_requests as db
import asyncio

app = Flask(__name__)

WHITELIST_IPS = {"127.0.0.1"}
model_classifier = ModelClassifier()


def classify_question(user_id: int, question: str, tool_type: str):
    _class = model_classifier.inference(question)
    asyncio.run(db.add_record(user_id=user_id, question=question, tool_type=tool_type, answer_id=_class))
    answer = asyncio.run(db.get_answer_by_id(_class))
    ans, = answer
    ans += "\r\n\r\nБолее подробную информацию можете найти на https://vk.com/club67592630?w=club67592630"
    return ans


@app.route("/classify", methods=["POST"])
def classify():
    client_ip = request.remote_addr
    if client_ip not in WHITELIST_IPS:
        return jsonify({"error": "Unauthorized IP"}), 403

    data = request.json
    if "question" not in data:
        return jsonify({"error": "Missing 'question' parameter"}), 400

    question = data.get("question")
    user_id = data.get("user_id")
    tool_type = data.get("tool_type")

    classification = classify_question(user_id, question, tool_type)
    return jsonify({"classification": classification})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5623)
