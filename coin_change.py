# quarter : 25 cents
# dime : 10 cents
# nickel : 5 cents
# penny : 1 cent

# write a function that returns the num of coins required
# to give a predefine number of cents.
import operator

cents = 31

coins = {
        'quarter': 25,
        'dime': 10,
        'nickel': 5,
        'penny': 1
}

def num_coins(cents):
    num_coins = 0

    for coin in sorted(coins.items(), key = operator.itemgetter(1),reverse=True):

        num_coins += cents//coin[1]
        cents = cents%coin[1]
        if not cents:
            return num_coins
        else:
            continue
    #return num_coins

if __name__=='__main__':
    print("coins required for %i cents : %i" %(cents,num_coins(cents)))
    #print(num_coins(32))

