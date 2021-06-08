from collections.abc import Iterable

def flatten(inp_list,ret):
    try:
        if isinstance(inp_list, Iterable):
            for x in inp_list:
                flatten(x, ret)
        else:
            ret.append(inp_list) 
    #print([x for temp in my_list for x in temp if isinstance(x, Iterable)])
    except TypeError as te:
        print(my_list, "is not iterable")
my_list = [(11,20,30),(40,50,60),(70,80,90),100]
#my_list = [10,20,30]
ret = []
flatten(my_list,ret)
print(ret)
