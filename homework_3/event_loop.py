from collections import deque
from exception_handler import ExceptionHandler


class EventLoop:
    def __init__(self):
        self.ready = deque()

    def add(self, func):
        self.ready.append(func)

    def run(self):
        while self.ready:
            func, event = self.ready.popleft()
            try:
                func()
            except Exception as e:
                ExceptionHandler().handle(event, e)
