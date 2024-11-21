from flask import Flask, render_template, request, jsonify, session
import pandas as pd
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

sentences = []

classes = {}


@app.route("/")
def index():
    session['current_sentence_index'] = 0  # Сброс индекса в начале
    return render_template("index.html", total=len(sentences))


@app.route("/get_sentence/<int:index>", methods=["GET"])
def get_sentence(index):
    if 0 <= index < len(sentences):
        session['current_sentence_index'] = index  # Запоминаем текущий индекс
        return jsonify({"sentence": sentences[index], "classes": classes, "index": index + 1, "total": len(sentences)})
    else:
        return jsonify({"message": "Все предложения обработаны!"})


@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute("""UPDATE samples SET label=?, notes=? WHERE value=?""", (data['class'], data['additionalInput'], data['sentence']))

    print("Полученные данные:", data)
    connect.commit()
    connect.close()
    return jsonify({"message": "Ответ сохранен!"})


if __name__ == "__main__":
    df = pd.read_csv("anses.csv")
    for i in df.iterrows():
        classes[i[1]['Категория']] = i[1]['Ответ']

    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute("""SELECT value FROM samples""")
    for i in cursor.fetchall():
        sentences.append(i[0])

    app.run(host="0.0.0.0", port=5050)
