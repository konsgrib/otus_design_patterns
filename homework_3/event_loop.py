from collections import deque

class EventLoop:
    def __init__(self):
        self.ready = deque()

    def add(self, func):
        self.ready.append(func)

    def run(self):
        while self.ready:
            event = self.ready.popleft()
            try:
                event[0]()
            except Exception as e:
                print("ERROR: ", type(e), "Event type: ", event[1])
