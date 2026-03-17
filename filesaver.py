class FileSaver:
    
    def __init__(self, src):
        try:
            open(src)

        except Exception:
            raise FileExistsError
        
        self.src = src

    def writeLine(self, drawingNum, nums, hitNums, winnings):
        with open(self.src) as file:
            file.write(f"Losowanie nr {drawingNum} - Wylosowano: {', '.join(nums)} Trafiono {len(hitNums)} liczby: {', '.join(hitNums)}. Wygrana: {winnings} PLN")

    def writeCustomLine(self, line):
        with open(self.src) as file:
            file.write(line)
