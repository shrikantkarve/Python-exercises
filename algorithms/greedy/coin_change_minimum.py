# quarter : 25 cents
# dime : 10 cents
# nickel : 5 cents
# penny : 1 cent

# write a function that returns the num of coins required
# to give a predefine number of cents.

# Problem is extended to find solution with minimum num of coins

import operator

cents = 32
coins = [25,10,5,1]

def num_coins(cents):
    lowest_num_coins = None
    lists = []
    #list_of_lists = [[list(coins).pop(x)] for x in range(len(coins)) ]
    for x in range(len(coins)):
        temp_list = [coins[a] for a in range(len(coins)) if a != x]
        lists.append(temp_list)
    
    for tlist in lists:
        #print(tlist)
        num_coins = 0
        amt = cents
        for coin in tlist:
            num_coins += amt//coin
            #print("num_coins : %i" % num_coins)
            #print(amt)
            amt = amt%coin
            if not amt:
                print("Possible solution: %i" % num_coins)
                if lowest_num_coins == None or lowest_num_coins > num_coins:
                    lowest_num_coins = num_coins
                break
            else:
                continue
                
    return lowest_num_coins

if __name__=='__main__':
    print("Minimum coins required for %i cents : %i" %(cents,num_coins(cents)))
