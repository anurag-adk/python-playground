import sys

def main():
    print(twoSum())
    # print(maxProfit())

def twoSum():
    nums = [2, 7, 11, 15]
    target = int(sys.argv[1])
    soln = {}
    for index, num in enumerate(nums):
        # print(index-1, soln)
        # print(target-num)
        if target - num in soln:
            return [soln[target - num], index]
        soln[num] = index

def maxProfit():
    prices = [7,1,5,3,6,4]
    min_price= float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        # print(min_price,end=",")
        profit = price - min_price
        # print(profit, end=",")
        max_profit = max(max_profit, profit)
        # print(max_profit)
    return max_profit

if __name__ == "__main__":
    main()