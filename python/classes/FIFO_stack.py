class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if not self.__queue:
            raise QueueError("Queue is empty")
        else:
            return self.__queue.pop()


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")