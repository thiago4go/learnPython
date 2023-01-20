import random

def play():
    user = input ("type:\n'r' for 👊\n'p' for 🖐️\n's' for ✌️\n")
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        return "It is a tie"
    elif who_win(user, computer):
        return "You won!"
    return "You lose!"

def who_win(player1, player2):
    if (player1 == "r" and player2 == "s" or\
        player1 == "s" and player2 == "p" or \
        player1 == "p" and player2 == "r"):
        return True

print(play())
