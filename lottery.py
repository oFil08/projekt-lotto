import random
import requests

class Lottery:

    def __init__(self, startingNums=[4, 9, 15, 22, 31, 37, 48, 56, 63, 74]):
        if not len(startingNums) == 10: raise IndexError

        self.url = "https://www.random.org/integers/"
        self.params = {
            "num": 1,
            "min": 1,
            "max": 80,
            "col": 1,
            "base": 10,
            "format": "plain",
            "rnd": "new",
            "replacement": 0
        }

        self.startingNums = startingNums

    def drawNumbers(self, api=False):
        nums = []

        if not api: nums = random.sample(range(1, 81), 20)
        else:
            for _ in range(20):
                while(True):
                    response = requests.get(self.url, params=self.params)
                    response.raise_for_status()
                    num = int(response.text)
                    if num not in nums:
                        nums.append(num)
                        break

        return sorted(nums)

    def checkHits(self, nums):
        hits = []

        for num in self.startingNums:
            if num in nums: hits.append(num)

        return hits
    
    def calculateWinnings(self, nums):
        winnings = [0, 0, 0, 0, 2, 4, 12, 140, 520, 10000, 250000]

        return winnings[len(self.checkHits(nums))]
