# coroutines are data consumers. Coroutines consume values which are sent to it.
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep('coroutine')
next(search)
search.send("What a day!")
search.send("What's happening")
search.send("I like coroutines instead!")
search.close()
# The sent values are accessed by yield. Why did we run next()? It is required in order to start the coroutine. Just like generators, coroutines do not start the function immediately. Instead they run it in response to the __next__() and .send() methods. Therefore, you have to run next() so that the execution advances to the yield expression.