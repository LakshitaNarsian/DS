class Array_Queue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self.data = [None] * Array_Queue.DEFAULT_CAPACITY

    def isEmpty(self):
        return self.size == 0

    def Front_enqueue(self, data):
        self.data.append(data)
        
    def Back_dequeue(self):
        return self.data.pop(0)

    def size(self):
        return len(self.data)

a=Array_Queue()

print(a.Front_enqueue('Lakshita'))
print(a.size())

