from flask import Flask, render_template

app = Flask(__name__)

@app.route("/get-high-score")
def get_high_score():
    with open("high_score.txt", "r") as f:
        high_score = f.read()
    return {"high_score": high_score}

@app.route("/set-high-score/<int:score>")
def set_high_score(score):
    old_high_score = None
    with open("high_score.txt", "r") as f:
        old_high_score = f.read()

    if old_high_score == "" or old_high_score == None:
        old_high_score = 0
    
    if score > int(old_high_score):
        with open("high_score.txt", "w") as f:
            f.write(str(score))
        return {"high_score": score}
    
    return {"high_score": old_high_score}

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    with open("high_score.txt", "a") as f:
        pass
    app.run(host="0.0.0.0", port=5509)