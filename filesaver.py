import os

class FileSaver:

    def __init__(self, src):
        if os.path.exists(src):
            open(f"{src}/logi.txt", "w").write("")
            open(f"{src}/statistics.txt", "w").write("")

        else: 
            os.mkdir(src)
            open(f"{src}/logi.txt", "x")
            open(f"{src}/statistics.txt", "x")
        
        self.src = src

    def writeLine(self, drawingNum, nums, hitNums, winnings):
        with open(f"{self.src}/logi.txt", "a") as file:
            file.write(f"Losowanie nr {drawingNum} - Wylosowano: {', '.join(map(str, nums))} Trafiono {len(hitNums)} liczby: {', '.join(map(str, hitNums))}. Wygrana: {winnings} PLN\n")

    def writeCustomLine(self, line):
        with open(f"{self.src}/logi.txt", "a") as file:
            file.write(line+"\n")

    def writeStatistics(self, iterations, winnings, hits):
        with open(f"{self.src}/statistics.txt", "a") as file:
            file.write(f"Koszty gier: {iterations * 2.50}\n")
            file.write(f"Wygrane: {winnings}\n")
            file.write(f"Bilans: {winnings - iterations * 2.50}\n")
            file.write(f"Srednia wygrana na kupon: {winnings/iterations}\n\n")
            
            for i, frequency in enumerate(hits):
                file.write(f"{i} liczb trafiono {frequency} razy ( {(frequency / iterations) * 100}% )\n") 
        

        
