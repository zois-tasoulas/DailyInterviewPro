class Queue:
    def __init__(self):
        self.main = []
        self.aux = []

    def enqueue(self, element):
        self.main.append(element)

    def dequeue(self):
        if not self.aux:
            while self.main:
                self.aux.append(self.main.pop())
        return self.aux.pop()

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(5)
    q.enqueue(6)
    print(q.dequeue())
    q.enqueue(7)
    print(q.dequeue())
    print(q.dequeue())
