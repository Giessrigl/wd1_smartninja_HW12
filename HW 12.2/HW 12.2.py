import random
import json
import datetime


current_time = datetime.datetime.now()
name = str(input("What's your name? \n"))
print(current_time)

# INPUT A ----------------------------------------------------------------------------------->
def play_game(level):
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())

    secret = random.randint(1, 10)
    attempts = 0
    wrong_guesses = []
    while True:
        guess = (input("guess the secret number (1-10): "))
        if guess.isdecimal() is True:
            guess_int = int(guess)
            attempts += 1
            if guess_int == secret:
                score_list.append(
                    {"level": level, "attempts": attempts, "date": str(datetime.datetime.now()), "name": str(name), "secret": str(secret),
                        "wrong_guesses": wrong_guesses})
                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))
                print("Congratulation! You win!")
                print("Attempts needed: " + str(attempts))
                break
            elif guess_int < secret:
                if level == "easy":
                    print("Wrong number! You need to go up!")
            elif guess_int > secret:
                if level == "easy":
                    print("Wrong number! You need to go down!")
            wrong_guesses.append(guess_int)
        else:
            print("Wrong input")
            continue

# INPUT B ------------------------------------------------------------------------------------>
def see_score():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
# LIST TOP SCORES OF EASY MODE -------------------------------------------------------------->
    print("Easy mode:")
    for i in range(len(score_list)):
        if score_list[i]["level"] == "hard":
            del score_list[i]
            break
    score_list_easy = sorted(score_list, key=lambda k: k["attempts"])[:3]
    for score_dict in score_list_easy:
        print("Top scores: " + (str(score_dict.get("attempts")) + " attempt(s), date: " + str(score_dict.get("date"))
                                + ", name: " + str(score_dict.get("name")) + ", number was: " + str(
                    score_dict.get("secret"))))

# LIST TOP SCORES OF HARD MODE ---------------------------------------------------------------->
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())

    print("Hard mode:")
    for i in range(len(score_list)):
        if score_list[i]["level"] == "easy":
            del score_list[i]
            break
    score_list_hard = sorted(score_list, key=lambda k: k["attempts"])[:3]
    for score_dict in score_list_hard:
        print("Top scores: " + (str(score_dict.get("attempts")) + " attempt(s), date: " + str(score_dict.get("date"))
                                + ", name: " + str(score_dict.get("name")) + ", number was: " + str(
                    score_dict.get("secret"))))




while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? \n")

    if selection.lower() == "a":
        while True:
            difficulty = input("Select Mode (easy/hard): ")
            if difficulty.lower() == "easy":
                play_game(level="easy")
                break
            elif difficulty.lower() == "hard":
                play_game(level="hard")
                break
            else:
                print("Wrong input")
                continue

    elif selection.lower() == "b":
        see_score()

    elif selection.lower() == "c":
        print("Goodbye " + str(name))
        break

    else:
        print("Wrong input")
        continue
