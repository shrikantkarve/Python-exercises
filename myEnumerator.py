class myEnumerator(object):
    def __init__(self, it):
        self.it = it
        self.index = 0

    def __iter__(self):
        try:
            print(f'In __iter__')
            self.it.__getattribute__("__iter__")
        except AttributeError:
            print("The argument passed, is not iterable")
            exit()

        return self

    def __next__(self):
        while True:
            #print("In next, value is : {} and index is : {}".format(i, self.index))
            self.index += 1

            if self.index > len(self.it):
                raise StopIteration
            
            return(self.index, self.it[self.index-1])
        #finally:
        #    raise StopIteration

myenum_ins = myEnumerator("abcd")
for index, val in myenum_ins:
    print(f'{index}: {val}')
        