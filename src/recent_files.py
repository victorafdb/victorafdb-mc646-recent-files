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
        self.blocked = False

    def is_full(self):
        if self.load == self.capacity:
            return True
        else:
            return False

    def searchForFileByPath(self, path):
        current = self.head
        while current:
            if current.path == path:
                return current
            current = current.next
        return None

    def append_head(self, opened_file):
        opened_file.next = self.head
        self.head = opened_file
        return

    def print_list(self):
        current = self.head
        while current is not None:
            current = current.next
        return

    def remove_and_return_file_in_the_middle(self, opened_file):

        current = self.head
        target = None

        if current.path == opened_file.path:
            return current

        while current.next.path != opened_file.path:
            current = current.next
        target = current.next
        current.next = target.next
        return target

    def remove_oldest_file(self):
        fast = self.head.next
        slow = self.head

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = None
        fast = None
        return

    def register_file(self, opened_file):

        # Check if Register file is blocked:
        if self.blocked:
            raise Exception("RecentFiles storage is blocked")
            return

        # If storage is full, remove oldest item and add the new one
        if self.is_full() is True:
            self.remove_oldest_file()
            self.append_head(opened_file)
            return

        # Check wether the file is already known by the RecentFiles
        file_exists = self.searchForFileByPath(opened_file.path)

        if file_exists:
            known_file = self.remove_and_return_file_in_the_middle(file_exists)
            self.append_head(known_file)
            return
        else:
            self.append_head(opened_file)
            self.load += 1
            return

    def flush(self):
        self.load = 0
        self.head = None

    def block(self):
        self.blocked = True

    def unblock(self):
        self.blocked = False
