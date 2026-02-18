class myEnumerator(object):
    def __init__(self, it):
        self.it = it
        # Python's enumerate starts at 0 by default
        self.index = -1

    def __iter__(self):
        try:
            # Check if iterable
            iter(self.it)
        except TypeError:
            print("The argument passed is not iterable")
            # Should raise error usually, but keeping print for now
            raise
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.it):
            raise StopIteration
        
        return (self.index, self.it[self.index])


if __name__ == "__main__":
    myenum_ins = myEnumerator("abcd")
    for index, val in myenum_ins:
        print(f'{index}: {val}')