from filesaver import *
from lottery import *

class LotteryManager:

    def __init__(self, src):
        self.saver = FileSaver(src)

    def massLottery(self, iterations, startingNums=[4, 9, 15, 22, 31, 37, 48, 56, 63, 74]):
        lottery = Lottery(startingNums)
        totalWinnings = 0
        hitsFrequency = [0 for _ in range(11)]
        
        for i in range(iterations):
            draw = lottery.drawNumbers()
            hits = lottery.checkHits(draw)
            winnings = lottery.calculateWinnings(draw)

            # zapisz wynik losowania do pliku
            self.saver.writeLine(i+1, draw, hits, winnings)

            # dodaj wygrane do siebie
            totalWinnings += winnings

            # 'logi' ilosci trafionych liczb
            hitsFrequency[len(hits)] += 1
            



