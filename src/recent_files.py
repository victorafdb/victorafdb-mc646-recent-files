# Recent Items .py
#
# Need to implement a RecentFiles class that maintains an a queue with
# the capability of:
# 1- If a file is opened and it is already inserted in the queue, it becomes the
# top file
# 2- The oldest item is removed when the queue is full and a new file is insert
# ed
# 3- Flush itself
# 4- Block the addition of new files

class File:
    def __init__(self, path, content):
        self.path = path
        self.content = content
        self.next = None


class RecentFiles:
    def __init__(self, capacity):
        self.capacity = capacity
        self.load = 0

    def is_full(self):
        return self.load == self.capacity
