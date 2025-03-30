from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize the game state
game_state = [""] * 9
X = "X"
O = "O"
turn = X


@app.route("/")
def index():
    global turn, game_state
    return render_template("index.html", turn=turn, play=game_state)


@app.route("/game", methods=["POST"])
def game():
    global turn, game_state
    i = int(request.form.get("cell_index"))  # Get the clicked cell index
    if game_state[i] == "":  # Only update if the cell is empty
        game_state[i] = turn
        turn = O if turn == X else X  # Switch turn
    return render_template("index.html", turn=turn, play=game_state)


@app.route("/reset", methods=["POST"])
def reset():
    global turn, game_state
    game_state = [""] * 9  # Reset the game state
    turn = X  # Reset the turn to X
    return render_template("index.html", turn=turn, play=game_state)


if __name__ == "__main__":
    app.run(debug=True)
