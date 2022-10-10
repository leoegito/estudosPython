import os


def clear(): return os.system('cls')


bids = {}
biddingFinished = False


def findHighestBidder(biddingRecord):
    highestBid = 0
    winner = ""
    for bidder in biddingRecord:
        bidAmount = biddingRecord[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highestBid}')


while not biddingFinished:
    name = input("What is your name? ")
    price = float(input("What is your bid? $"))
    bids[name] = price
    shouldContinue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if shouldContinue == "no":
        biddingFinished = True
        findHighestBidder(bids)
    elif shouldContinue == "yes":
        clear()
