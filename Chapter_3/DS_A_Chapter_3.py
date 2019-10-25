

class Stack:    #Assumes that the end of the list will hold the top element of the stack. As the stack grows (as push
                #operations occur), new items will be added to the end of the list. Pop() operations will manipulate
                #that same end
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

#Note: we could have chosen to implement the stack using a list where the top is the beginning instead of at the end
#If we did this --> the pop and append methods would no longer work and we would have to index position 0 (the first
#item in the list) explicitly using pop and insert

#Next we will use a stack to determine if pair(s) of parentheses are balanced using a LIFO methodology (the first
#opening symbol processed may have to wait until the very last symbol for its match) --> closing symbols match
#opening symbols in the reverse order of their appearance; they match from the inside out. As a result, a stack
#is the perfect data structure for keeping hte parentheses

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

#The function parChecker assumes that a Stack class exists and returns a boolean result as to whether a pair of
#parentheses is balanced. The algorithm functions by starting with an empty stack --> if a symbol is an opening
#parentheses, push it to the stack as a signal that a corresponding closing symbol needs to appear later. If the
#symbol is a closing parentheses, pop the stack. As long as its possible to pop the stack to match every closing
#symbol, the parentheses remain balanced but if at any time there is no opening symbol on the stack to match a closing
#symbol, the string is not balanced properly. The stack should be empty at the end when all symbols have been processed

#We can implement a more general version that considers balanced brackets and curly braces as well, as is shown below

def parCheckerGeneral(symbolString):
    s = Stack()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"

    return opens.index(open) == closers.index(close)

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

if __name__ == "__main__":

    s = Stack()
    s.isEmpty()
    print(s.isEmpty())

    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    s.pop()
    s.pop()
    print(s.size())

    #Consider the performance of the two "Stack" implementations --> Recall: append and pop() operations are
    #both O(1) while the second implementation suffers in that insert(0) and pop(0) operations require O(n) for
    #a stack of size "n" --> the benchmarking of both implementations will have different timings

    #Testing Git repo.....