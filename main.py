from filesaver import *
from lotteryManager import*

for i in range(10):
    LotteryManager.massLottery(f"loteria{i+1}", 100000)