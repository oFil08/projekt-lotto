import random

class Lottery:

    def __init__(self, startingNums):
        if not len(startingNums) == 10: raise IndexError

        self.startingNums = startingNums

    def drawNumbers(self):
        nums = []

        for _ in range(20):
            while True:
                randNum = random.randint(1, 80)
                if not randNum in nums: break
            
            nums.append(randNum)

        return sorted(nums)

    def checkHits(self, nums):
        hits = []

        for num in self.startingNums:
            if num in nums: hits.append(num)

        return hits
    
    def calculateWinnings(self, nums):
        winnings = [0, 0, 0, 0, 2, 4, 12, 140, 520, 10000, 250000]

        return winnings[len(self.checkHits(nums))]
