from filesaver import *
from lotteryManager import *
from lottery import *

DEFAULT_ITERATIONS = 10000
DEFAULT_LOTERIES = 10
l = Lottery()

print("test losowań:\n")
for _ in range(10):
    print(l.drawNumbers(True))

api = (str(input("\n\n### TEST MULTI MULTI ###\n\nUżyć api? [y/N] (ostreżenie, jedno losowanie z api to ~10 sekund aby obejść limit xD)\n")).lower() == "y")

iterations = 10000
numOfLoteries = 10

while True:
    try:
        iterations_input = input(f"ile iteracji [{DEFAULT_ITERATIONS}]?\n").strip()
        iterations = int(iterations_input) if iterations_input else DEFAULT_ITERATIONS

        num_input = input(f"ile razy? [{DEFAULT_LOTERIES}]\n").strip()
        numOfLoteries = int(num_input) if num_input else DEFAULT_LOTERIES

        break

    except ValueError:
        print("Podaj poprawne liczby!")
nums = [4, 9, 15, 22, 31, 37, 48, 56, 63, 74]

if input("użyć domyślnych liczb? [Y/n]\n").lower() == "n":
    while(nums == []):
        nums = list(map(int, data)) if len(data := input().split()) <= 10 else []

for i in range(numOfLoteries):
    LotteryManager.massLottery(f"loteria{i+1}", iterations, api, nums)
