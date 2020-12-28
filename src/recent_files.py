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
        if capacity < 1:
            raise ValueError(
                "RecentFiles storage capacity must be > 1")
        self.capacity = capacity
        self.load = 0
        self.head = None

    def is_full(self):
        return self.load == self.capacity

    def searchForFileByPath(self, path):
        current = self.head
        while current:
            if current.path == path:
                return current
        return None

    def register_file(self, opened_file):
        file_exists = self.searchForFileByPath(opened_file.path)
        if file_exists is not None:
            opened_file.next = self.head
            self.head = opened_file
        else:
            current = self.head

            if current is None:
                self.head = opened_file
            else:
                while current.next:
                    current = current.next
                current.next = opened_file

            self.load += 1
            return
