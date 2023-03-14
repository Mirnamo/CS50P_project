import random


def main():
    print("which game would you like to play? \n game 1 \n game 2 \n game 3")
    answer = str(input("Game: "))
    if answer == "game 1":
        print("Which one do you choose? rock, paper, scissors?")
        play = input("choice: ")
        print(game1(play))
    elif answer == "game 2":
        print("choose a level: 1, 2, 3")
        string = int(input("level: "))
        print(game2(string))
    elif answer == "game 3":
        print("Guess the animal, are u ready?")
        response = input("... ")
        print(game3(response))


def game1(choose):
    i = 0
    choice = ["rock", "paper", "scissors"]

    print(f"choose from list {choice}")

    result = random.choice(choice)

    if (
        (choose == "rock" and result == "rock")
        or (choose == "paper" and result == "paper")
        or (choose == "scissors" and result == "scissors")
    ):
        i += 1
        print(result)
        return "even"

    elif choose == "rock" and result == "scissors":
        print(result)
        return "you win"

    elif choose == "paper" and result == "rock":
        print(result)
        return "you win"

    elif choose == "scissors" and result == "paper":
        print(result)
        return "you win"

    elif choose == "rock" and result == "paper":
        print(result)
        i += 1
        return "you lose"
    elif choose == "scissors" and result == "rock":
        print(result)
        i += 1
        return "you lose"
    elif choose == "paper" and result == "scissors":
        print(result)
        i += 1
        return "you lose"
    if i == 3:
        return "Thank you for playing with me!"


def game2(string):
    if string == 1:
        nums = range(1, 10)
        mylist = list(map(int, nums))
        n1 = int(random.choice(mylist))
        n2 = int(random.choice(mylist))
        print(f"solve: {n1} x {n2}")
        result = n1 * n2
        while True:
            try:
                answer = int(input("what's your answer? "))
                if answer == result:
                    return "Good job!"
                else:
                    print("Wrong answer")
                    pass
            except ValueError:
                raise

    elif string == 2:
        nums = range(10, 100)
        mylist = list(map(int, nums))
        n1 = int(random.choice(mylist))
        n2 = int(random.choice(mylist))
        print(f"solve: {n1} x {n2}")
        result = n1 * n2
        while True:
            try:
                answer = int(input("what's your answer? "))
                if answer == result:
                    return "Good job!"
                else:
                    print("Wrong answer")
                    pass
            except ValueError:
                raise

    elif string == 3:
        nums = range(100, 1000)
        mylist = list(map(int, nums))
        n1 = int(random.choice(mylist))
        n2 = int(random.choice(mylist))
        print(f"solve: {n1} x {n2}")
        result = n1 * n2
        while True:
            try:
                answer = int(input("what's your answer? "))
                if answer == result:
                    return "Good job!"
                else:
                    print("Wrong answer")
                    pass
            except ValueError:
                raise


def game3(response):
    response = response.lower()
    if "yes" in response:
        guess = [
            "has a long neck",
            "the king of the jungle",
            "scary big and fast cat",
            "big enough to crash all animals",
            "cute little mermaid in sea and ocean",
        ]
        guesses = random.choice(guess)
        print(guesses)
        while True:
            try:
                animal = input("answer: ")
                animal = animal.lower()
                if guesses == "has a long neck" and animal == "giraffe":
                    return "correct"
                elif guesses == "the king of the jungle" and animal == "lion":
                    return "correct"
                elif guesses == "scary big and fast cat" and animal == "tiger":
                    return "correct"
                elif (
                    guesses == "big enough to crash all animals"
                    and animal == "elephant"
                ):
                    return "correct"
                elif (
                    guesses == "cute little mermaid in sea and ocean"
                    and animal == "dolphin"
                ):
                    return "correct"
                else:
                    print("Wrong answer")
                    pass
            except ValueError:
                raise


if __name__ == "__main__":
    main()
