"""
Data Structure Implementation: Build your own implementation of a stack or queue data structure with appropriate methods.
"""

class Stack:
    def __init__(self):
        self._stack = []

    def stack(self):
        return self._stack

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self._stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self._stack[-1]
        return None

    def is_empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)


class Queue:
    def __init__(self):
        self._queue = []

    def queue(self):
        return self._queue

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self._queue.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self._queue[0]
        return None

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)


