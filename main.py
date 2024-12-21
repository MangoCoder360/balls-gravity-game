from flask import Flask, render_template, request
import json

app = Flask(__name__)

def get_leaderboard_from_json():
    with open("leaderboard.json", "r") as f:
        unsorted = json.load(f)
        sorted_leaderboard = sorted(unsorted, key=lambda x: x["score"], reverse=True)
        return sorted_leaderboard

def append_score_to_leaderboard(name, score):
    leaderboard = get_leaderboard_from_json()
    leaderboard.append({"name": name, "score": score})
    with open("leaderboard.json", "w") as f:
        json.dump(leaderboard, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-leaderboard')
def get_leaderboard():
    return get_leaderboard_from_json()

@app.route('/submit-score')
def submit_score():
    name = request.args.get('name')
    score = int(request.args.get('score'))
    append_score_to_leaderboard(name, score)
    return get_leaderboard_from_json()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5509)