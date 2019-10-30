import string


class Stack:  # Assumes that the end of the list will hold the top element of the stack. As the stack grows (as push
    # operations occur), new items will be added to the end of the list. Pop() operations will manipulate
    # that same end
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Note: we could have chosen to implement the stack using a list where the top is the beginning instead of at the end
# If we did this --> the pop and append methods would no longer work and we would have to index position 0 (the first
# item in the list) explicitly using pop and insert

# Next we will use a stack to determine if pair(s) of parentheses are balanced using a LIFO methodology (the first
# opening symbol processed may have to wait until the very last symbol for its match) --> closing symbols match
# opening symbols in the reverse order of their appearance; they match from the inside out. As a result, a stack
# is the perfect data structure for keeping hte parentheses

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


# The function parChecker assumes that a Stack class exists and returns a boolean result as to whether a pair of
# parentheses is balanced. The algorithm functions by starting with an empty stack --> if a symbol is an opening
# parentheses, push it to the stack as a signal that a corresponding closing symbol needs to appear later. If the
# symbol is a closing parentheses, pop the stack. As long as its possible to pop the stack to match every closing
# symbol, the parentheses remain balanced but if at any time there is no opening symbol on the stack to match a closing
# symbol, the string is not balanced properly. The stack should be empty at the end when all symbols have been processed

# We can implement a more general version that considers balanced brackets and curly braces as well, as is shown below

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


def matches(open, close):
    opens = "([{"
    closers = ")]}"

    return opens.index(open) == closers.index(close)


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


# The function below implements the "Divide by 2" algorithm. It takes an argument that is a decimal number and repeatedly
# divides it by 2.

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2  # <-- Integer Division

    binString = " "
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


# We can modify the "Divide by 2" function to divide by any base using a more general "Divide by Base" function, as
# shown below. The function takes a decimal number and any base between 2 and 16 as parameters. The remainders are
# still pushed unto the stack until the remainder reaches zero with the same left-to-right construction technique with
# a slight change in that, as we get to 10, we can't simply use the remainder as they are themselves represented as
# two digit numbers --> we instead have to create a set of digits that can be used to represent those remainder
# beyond 9 --> SOLUTION: extend the digit set to include some alphabet characters --> Example: hexadecimal uses the
# ten decimal digits along with the first six alphabet characters for the 16 digits. To implement this, a digit string
# is created that stores the digits in their corresponding positions. 0 is at position 0, 1 is at position 1, A is at
# position 10, B is at position 11 and so on. When a remainder is removed from the stack, it can be used to index into
# the digit string and the correct resulting digit can be appended to the answer

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = " "
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


# This code uses a dictionary called "prec" to hold the precedence of operators for the code that converts an infix
# operation to a postfix operation. The dictionary maps each operator to an integer that can be compared against the
# precedence levels of other operators. The left parenthesis will receive the lowest value possible so that any
# operator that is compared against it will have higher precedence and will be placed on top of it.
# Ex: + --> 1, * --> 2, / --> 3 as an example

def infixToPostfix(infixexpr):
    prec = {}  # Dictionary for holding precedence of operators
    prec["*"] = 3  # Setting the precedence of operators using a dictionary where the operators are the keys
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()  # Create a stack for storing the operators
    postfixList = []  # Create a list for storing the output. This is what will be output

    tokenList = infixexpr.split()  # I'm guessing this splits the expression using a delimeter...

    for token in tokenList:
        if token in string.ascii_uppercase:  # If the token is a string add it to the output list
            postfixList.append(token)
        elif token == '(':  # If the token is a left parenthesis, push it to the stack for storing tokens
            opStack.push(token)
        elif token == ')':  # If the token is a right parenthesis, pop the operator stack until left parenthesis reached
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:  # I believe this section of the code is for checking the opstack for operators and removing and replacing
            # those with higher or equal precedence and appending them to the output list
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    # We then check the opstack and add any remaining operators in the stack to the output list
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)  # Joins elements of string with a space between them (member of "string" class)


# Note: having or not having spaces in the input to the infixToPostfix function can causes problems and should be
#      modified. The function should take a general format, no matter how many white spaces

# This function converts a postfix expression to an equivalent arithmetic outcome using a helper function doMath

def postfixEval(postfixExpr):
    operandStack = Stack()

    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)

    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


# IMPORTANT: Both the postfix conversion and postfix evaluation programs assumed no input error --> they could use
#           error detection in future versions

# Create a class for the implementation of the abstract data type queue. We can use the power and simplicity of the list
# The rear is going to be the 0 index of the list --> allows us to use the insert function on the list to add new
# elements to the rear of the queue. The pop oepration can remove elements from the front (last element of the list).
# This means that the enqueue method will be O(n) and dequeue will be O(1)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):  # Order O(n)
        self.items.insert(0, item)

    def dequeue(self):  # Order O(1)
        return self.items.pop()

    def size(self):
        return len(self.items)


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


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

    # Consider the performance of the two "Stack" implementations --> Recall: append and pop() operations are
    # both O(1) while the second implementation suffers in that insert(0) and pop(0) operations require O(n) for
    # a stack of size "n" --> the benchmarking of both implementations will have different timings

    # Testing Git repo.....
    number = divideBy2(223)
    print(number)

    number2 = baseConverter(1023, 16)
    print(number2)

    list1 = infixToPostfix("( A + B ) * ( C + D )")
    # For list1:
    #   Add left parenthesis to opStack
    #   Add "A" to output
    #   Add "+" to opStack
    #   Add "B" to output
    #   Since we've reached the right parenthesis, pop the opStack until the left parenthesis is removed and add each
    #   operator to the end of the list. "+" would go to the output (so far, A, B and + are in the output
    #   Add "*" to the opStack
    #   Add "(" to the opStack
    #   Add "C" to the output
    #   Add "+" to the opStack
    #   Add "D" to the output
    #   Since we've reached another right parenthesis, pop the opStack until the left parenthesis is removed. We have a
    #   "+" in the opStack so we add that to the output and we should reach a left parenthesis. So the output should
    #   have A, B, +, C, D, +
    #   Since "*" is left in opStack, append that to the end of the output

    list2 = infixToPostfix("( A + B ) * C")
    list3 = infixToPostfix("A + B + C")

    print(list1)
    print(list2)
    print(list3)

    # Note: Python raises a KeyError whenever a dict() object is requested (using the format a = adict[key])
    #      and the key is not in the dictionary

    q = Queue()
    print(q.isEmpty())
    q.enqueue('dog')
    q.enqueue(4)
    q = Queue()
    print(q.isEmpty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q)
    print(q.size())
    print(q.isEmpty())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())

    # RECALL: Page 73 in the book details the Big-O efficiency of different operations

    # Implementation of a "Hot Potato" game using a Queue abstract data type
    remainingPerson = hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
    print(remainingPerson)

    # Notice that the first name in the list is the first loaded into the queue using the "enqueue()" function --> Bill
    # is the first item in the list and the first to be enqueued into the Queue (he moves to the front of the queue)