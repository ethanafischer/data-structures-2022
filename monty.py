import random


def cycle() -> int:
    doors = ["Goat", "Goat", "Goat"]
    carDoor = random.randint(0, 2)
    print("cardoor", carDoor)
    doors[carDoor] = "Car"
    print("doors", doors)
    playerChoice = random.randint(0, 2)
    playerPick = doors[playerChoice]
    print("player chooses:", playerChoice)
    removeGoatDoor = random.choice([i for i in range(0, 3) if i not in [playerChoice, carDoor]])
    print("show goat door", removeGoatDoor)
    doors.pop(removeGoatDoor)
    print(doors)

    if playerPick == "Car":  # IF SWAP:
        return 1  # loss
    else:
        return 0  # win

count = 0
for i in range(1000):

    if cycle() == 1:
        count += 1
print(count / 1000)