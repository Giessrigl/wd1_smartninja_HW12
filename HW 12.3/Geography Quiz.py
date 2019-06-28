import random

countries = ["Austria", "Belgium", "Croatia", "Germany"]
countries_cities = {"Austria": "Vienna", "Belgium": "Brussels", "Croatia": "Zagreb", "Germany": "Berlin"}

while True:
    question = random.choice(countries)
    guess = input("What is the capital of " + str(question) + ": ")
    if guess == countries_cities[question]:
        print("You are right!")
        ask = input("Another round? (y/n): ")
        if ask == "n":
            break
    else:
        print("You are wrong!")



