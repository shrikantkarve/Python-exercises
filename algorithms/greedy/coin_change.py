# quarter : 25 cents
# dime : 10 cents
# nickel : 5 cents
# penny : 1 cent

# write a function that returns the num of coins required
# to give a predefine number of cents.
import operator

cents = 33

default_coins = {
    'quarter': 25,
    'dime': 10,
    'nickel': 5,
    'penny': 1
}


def num_coins(cents, coins=None):
    if coins is None:
        coins = default_coins

    num_coins = 0

    for coin_name, coin_value in sorted(coins.items(), key=operator.itemgetter(1), reverse=True):
        num_coins += cents // coin_value
        cents = cents % coin_value
        if not cents:
            return num_coins
    
    # If we exit loop and cents > 0, we can't make exact change with given coins
    # But for standard US coins (with penny=1), this shouldn't happen for integer cents
    return num_coins


if __name__ == '__main__':
    print("coins required for %i cents : %i" % (cents, num_coins(cents)))
