
# BEYOND THE EXERCISE
# In this exercise, we saw how we can combine user-supplied data with additional information from the system. Here are some more exercises you can try to get additional practice writing such generator functions:

# The existing function elapsed_since reported how much time passed between iterations. Now write a generator function that takes two arguments--a piece of data and a minimum amount of time that must elapse between iterations. If the next element is requested via the iterator protocol (i.e., next), and the time elapsed since the previous iteration is greater than the user-defined minimum, then the value is returned. If not, then the generator uses time.sleep to wait until the appropriate amount of time has elapsed.

# Write a generator function, file_usage_timing, that takes a single directory name as an argument. With each iteration, we get a tuple containing not just the current filename, but also the three reports that we can get about a file’s most recent usage: its access time (atime), modification time (mtime), and creation time (ctime). Hint: all are available via the os.stat function.

# Write a generator function that takes two elements: an iterable and a function. With each iteration, the function is invoked on the current element. If the result is True, then the element is returned as is. Otherwise, the next element is tested, until the function returns True. Alternative: implement this as a regular function that returns a generator expression.