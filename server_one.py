from flask import Flask
import random

server_flask = Flask(__name__)
ANSWER = random.randint(0, 100)
print(f"The answer is {ANSWER}")


def more_or_less(diff):
    if diff < 0:
        return "<h2>Hint: Guess something lesser<h2>"
    elif diff > 0:
        return "<h2>Hint: Guess something higher"


def how_close(diff):
    if abs(diff) < 10:
        return "<h1><b>Your very close</b></h1>" \
               "<img src='https://media.giphy.com/media/MWSRkVoNaC30A/giphy-downsized-large.gif' width=500>" \
               f"{more_or_less(diff)}"
    elif abs(diff) < 20:
        return "<h1><b>Come on, Your close</b></h1>" \
               "<img src='https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif' width=500>" \
               f"{more_or_less(diff)}"
    elif abs(diff) < 30:
        return "<h1><b>Not so close</b></h1>" \
               "<img src='https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif' width=500>" \
               f"{more_or_less(diff)}"
    else:
        return "<h1><b>Your so far</b></h1>" \
               "<img src='https://media.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif' width=500>" \
               f"{more_or_less(diff)}"


@server_flask.route('/')
def display_page():
    return "<h1><b>GUESS A NUMBER BETWEEN 0 TO 100</b></h1>" \
           "<h1><b>FIND ME!</b></h1>" \
           "<img src='https://media.giphy.com/media/8vQSQ3cNXuDGo/giphy.gif' width=500>"


@server_flask.route('/<number>')
def guess_a_number(number):
    if int(number) == ANSWER:
        return "<h1>Ooooo YOU GOT ME!</h1>" \
               "<img src='https://media.giphy.com/media/S6VGjvmFRu5Qk/giphy.gif' width=500>"
    else:
        difference = ANSWER - int(number)
        return how_close(diff=difference)


if __name__ == "__main__":
    server_flask.run(debug=True)
