import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result

    return wrapper


# 1 способ: с помощью списка реализуем буфер FIFO, + = простота использения, - = для операций push, pop,
# time complexity = O(n)
class FIFO_List:
    def __init__(self):
        self.fl = []
        self.size = 0

    def push(self, value):
        self.fl.append(value)
        self.size += 1

    def pop(self):
        if len(self.fl) == 0:
            return None
        self.size -= 1
        return self.fl.pop(0)


# Второй способ - построение связанного списка, в котором time complexity для операций push, get = O(1),
# является более оптимальным в терминах Time Complexity
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class FIFO_Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def get_and_pop(self):
        if self.size == 0:
            return None
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value


@timer
def list_time():
    l1 = FIFO_List()
    for i in range(10 ** 5):
        l1.push(i)
    while l1.size > 0:
        l1.pop()


@timer
def queue_time():
    q1 = FIFO_Queue()
    for i in range(10 ** 5):
        q1.push(i)
    while q1.size > 0:
        q1.get_and_pop()


if __name__ == '__main__':
    list_time()
    queue_time()
