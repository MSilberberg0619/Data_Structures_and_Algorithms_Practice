
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

    #Testing Git repo...