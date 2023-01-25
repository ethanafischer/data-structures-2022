import random

rolltable = []
avgrolls = []
onecyclerolls = []
cycleinfo = []


def coinflip() -> tuple[bool, bool, str]:
    coin = random.randint(0, 1)
    if coin == 0:
        return True, False, "WON"  # won the 50/50
    else:
        return False, True, "LOST"  # lost the 50/50


def cycle(win, counter, lostCoinFlip):
    info = []
    totalOneCycle = 0
    while win is False:
        roll = random.uniform(0, 1)
        counter += 1
        totalOneCycle += 1
        info.append([totalOneCycle, roll])

        if counter == 76:
            odds = 0.20627
        elif counter == 77:
            odds = 0.13946
        elif counter == 78:
            odds = 0.09429
        elif counter == 79:
            odds = 0.06375
        elif counter == 80:
            odds = 0.04306
        elif counter == 81:
            odds = 0.02914
        elif counter == 82:
            odds = 0.01970
        elif counter == 83:
            odds = 0.01332
        elif counter == 84:
            odds = 0.00901
        elif counter == 85:
            odds = 0.0608
        else:
            odds = 0.006

        if counter == 180:
            win, lostCoinFlip, i = True, False, "WON"
            rolltable.append([counter, roll, i])

        if roll <= odds or counter == 90:
            if lostCoinFlip is False:
                win, lostCoinFlip, i = coinflip()
                rolltable.append([counter, roll, i])
                counter = 0

            else:
                win, lostCoinFlip, i = True, False, "WON"
                rolltable.append([counter, roll, i])
    cycleinfo.append(info)
    return totalOneCycle



cycles = 100000 #ANSWER: 42%, 41.35%

win = False
counter = 0
lostCoinFlip = False

for i in range(cycles):
    onecyclerolls.append(cycle(win, counter, lostCoinFlip))


print("\ntotal number of cycles:", cycles)
"""print("coinflips:")
for i in rolltable:
    print("roll " + str(i[0]) + ": " + str(i[1]) + " " + str(i[2]))

"""
for j in rolltable:
    if j[2] == "WON":
        avgrolls.append(j[0])

avgcount = 0
for k in avgrolls:
    if k < 90:
        avgcount += 1

print("percent of wins under 90:", avgcount, "/", len(avgrolls), "=", avgcount / len(avgrolls))

"""userin = input("\n\nroll log:\nexpand? y/n: ")
if userin == "y":
    print("==========================")
    for i in range(len(cycleinfo)):
        print("cycle", i + 1)
        print("total rolls before win:", onecyclerolls[i])
        for j in range(len(cycleinfo[i])):
            print(str(cycleinfo[i][j]).replace('[', '').replace(']', '').replace(',', '.'))
        print("==========================")
"""
print(onecyclerolls)