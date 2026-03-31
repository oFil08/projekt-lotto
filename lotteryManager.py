from filesaver import *
from lottery import *

class LotteryManager:
    def massLottery(src, iterations, api, startingNums=[4, 9, 15, 22, 31, 37, 48, 56, 63, 74]): 
        saver = FileSaver(src)

        lottery = Lottery(startingNums)
        totalWinnings = 0
        hitsFrequency = [0 for _ in range(11)]
        
        for i in range(iterations):
            draw = lottery.drawNumbers()
            hits = lottery.checkHits(draw)
            winnings = lottery.calculateWinnings(draw)

            # zapisz wynik losowania do pliku
            saver.writeLine(i+1, draw, hits, winnings)

            # dodaj wygrane do siebie
            totalWinnings += winnings

            # 'logi' ilosci trafionych liczb
            hitsFrequency[len(hits)] += 1

        saver.writeStatistics(iterations, totalWinnings, hitsFrequency)

        
            



