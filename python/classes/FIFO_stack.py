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
class Extended(Queue):
    def is_empty(self):
        try:
            item = self.get()
            self.put(item)
            return False
        except QueueError:
            return True



que = Extended()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.is_empty():
        print(que.get())
    else:
        print("Queue empty")


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")