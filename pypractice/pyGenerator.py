""" 
# Generators resume execution
# Generators can maintain state in local variables
# Generators facilitate complex control flow
# Generators are lazy evaluators
"""


def take(count, iterable):
    "Take first count elements"
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def distinct(iterable):

    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_take():
    items = [2, 4, 6, 8, 10, 12]
    for item in take(3, items):
        print(item)

def getDistinct():
    items = [5, 6, 7, 5, 3, 3, 3]
    for item in distinct(items):
        print(item)

# return first 3 unique items from a list
def pipeline():
    items = [5, 6, 6, 5, 3, 3, 7, 1]
    for item in take(5, distinct(items)):
        print(item)


if __name__ == "__main__":
    #run_take()
    #getDistinct()
    pipeline()