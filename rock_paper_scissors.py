import random

def play():
    user = input("Choose a rock (r), scissors (s) or paper (p): ")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return 'A draw!'

    if is_win(user, computer):
        return 'You\'ve won!'

    return 'The computer won!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True
    return False

print(play())
