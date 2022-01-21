
def main():
    # 54 with jokers
    remaining = 52
    cards = {"d":[], "h":[],"c":[],"s":[]}
    face = ["j","q", "k", "a"]
    face_vals = {"j":11,"q":12, "k":13, "a":14}
    dealt = 0

    # [2,3,4,5,6,7,8,9,10,"j","q","k", "a"]
    # [2,3,4,5,6,7,8,9,10,11, 12,  13,  14]

    for i in range(2, 15):
        for key in cards.keys():
            cards[key].append(i)

    def oddsColor(color):
        # add zero check
        if color == "r":
            return (len(cards["d"]) + len(cards["h"])) / remaining
        else:
            return (len(cards["c"]) + len(cards["s"])) / remaining

    def oddsHigher(card):
        count = 0
        for key in cards.keys():
            for car in cards[key]:
                if car > card:
                    count += 1
        return count / remaining

    def oddsLower(card):
        count = 0
        for key in cards.keys():
            for car in cards[key]:
                if car < card:
                    count += 1
        return count / remaining

    def outSide(one, two):
        if one > two:
            left, right = two, one
        else:
            left, right = one, two

        return oddsLower(left) + oddsHigher(right)

    def inside(one, two):
        # fix with math
        count = 0
        if one > two:
            left, right = two, one
        else:
            left, right = one, two
        
        # return oddsHigher(left) - oddsLower(right)
        for key in cards.keys():
            for card in cards[key]:
                if card > left and card < right:
                    count += 1
        return count / remaining

    def suite(suite):
        return len(cards[suite]) / remaining

    def remove(card):
        # cards by number/face + suit
        # kh = king of hearts

        suit = card[-1]
        val = card[0:len(card) - 1]
        num = 0
        if val.isdigit():
            num = int(val)
        else:
            num = face_vals[val]

        for i,value in enumerate(cards[suit]):
            if value == num:
                cards[suit].pop(i)
                break

    def getCardVal(card):
        suite = card[-1]
        val = card[0:len(card) - 1]
        # print(suite, val)
        if val.isdigit():
            return int(val)
        else:
            return face_vals[val]
    
    # print(suite("h"))
        
    card = input("press enter to start")

    # first input is r or b
    # second is high low
    # third is in or out
    # fourth d, h, c, or s

    while card != "q" and remaining >= 4:
        hand = []
        for i in range(4):
            if i == 0:
                print("red: " + str(oddsColor("r")))
                print("black: " + str(oddsColor("b")))
            elif i == 1:
                
                print("higher: " + str(oddsHigher(hand[0])))
                print("lower: " + str(oddsLower(hand[0])))
                print("tie: " +  str(1 - oddsLower(hand[0]) - oddsHigher(hand[0])))
            elif i == 2:
                print("inside: " + str(inside(hand[0], hand[1])))
                print("outside: " + str(outSide(hand[0], hand[1])))
                print("tie: " +  str(1 - outSide(hand[0], hand[1]) - inside(hand[0], hand[1])))
            elif i == 3:
                print("diamonds: " + str(suite("d")))
                print("hearts: " + str(suite("h")))
                print("clubs: " + str(suite("c")))
                print("spades: " + str(suite("s")))

            print(" ")
            throw = input("throw?: ")
            while throw != "y" and throw != "n":
                throw = input("type y for yes n for no")
            
            dealt_value= input("enter dealt card value: ")
            dealt_suit = input("enter card suit: ")
            hand.append(getCardVal(dealt_value + dealt_suit))
            remove(dealt_value + dealt_suit)

            remaining -= 1
            dealt += 1

            if throw == "y":
                break

            print("remaining: " + str(remaining))
            print("dealt: " + str(dealt))
            print(" ")
    
    def messyGame():
        while card != "q" and remaining >= 4:
            hand = []
            for i in range(4):
                # guess = input("guess ")
                if i == 0:
                    guess = input("type r for red and b for black: ")
                    while guess != "r" and guess != "b":
                        print(guess)
                        guess = input("type r for red and b for black: ")
                    print(oddsColor(guess))
                elif i == 1:
                    while guess != "hi" and guess != "low":
                        guess = input("type hi for higher and low for lower: ")
                    if guess == "hi":
                        print("odds for a higher card: " + str(oddsHigher(hand[0])))
                    else:
                        print("odds for a lower card: " + str(oddsLower(hand[0])))
                elif i == 2:
                    while guess != "in" and guess != "out":
                        guess = input("type in for in range and out for out of range: ")
                    if guess == "in":
                        print("odds for a card in range: " + str(inside(hand[0], hand[1])))
                    else:
                        print("odds for a card outside: " + str(outSide(hand[0], hand[1])))
                    # print(oddsColor(guess))
                elif i == 3:
                    while guess != "d" and guess != "h" and guess != "c" and guess != "s":
                        guess = input("type d for diamond h for hearts c for clubs and s for spades: ")
                    print(suite(guess))
                print(" ")
                
                dealt_value= input("enter dealt card value: ")
                dealt_suit = input("enter card suit: ")
                hand.append(getCardVal(dealt_value + dealt_suit))
                remove(dealt_value + dealt_suit)

                card = guess
                remaining -= 1
                dealt += 1


if __name__ == "__main__":
        main()