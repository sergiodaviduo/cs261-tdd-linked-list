# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# YOUR NAME

class LinkedList:

    addr = None

    def __init__(self, value=None):
        self.value = value
        self.addr = self
        self.next = self
        self.prev = self

    def is_sentinel(self):
        if(self.value == None):
            return True
        else:
            return False

    def is_empty(self):
        if self.addr != self or self.next != self or self.prev != self:
            print("not empty")
            return False
        else:
            print("empty")
            return True

    def is_last(self):
        if self.is_empty():
            return True
        elif self.prev.value == self:
            return True

    def last(self):
        if self.is_empty():
            return self;
        return self.prev

    def append(self, appended):
        print("appending")
        if self.is_empty():
            print("appending empty")
            self.next = appended
            self.prev = appended
            appended.prev = self
            appended.next = self
            self.value = appended
        elif self.last() == self.prev:
            print("appending non-empty")
            self.next.next = appended
            appended.prev = self.next


    pass
