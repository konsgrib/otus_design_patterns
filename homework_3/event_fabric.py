import time
import random
from abc import ABC


class AbstractEvent(ABC):
    def run(self):
        n = random.randint(0, 5)
        exceptions = [ZeroDivisionError, KeyError, IndexError]
        list_length = len(exceptions) - 1
        time.sleep(1)
        if n > list_length:
            print(f"Event type: {self.__class__.__name__} called, NORMAL EVENT")
            return
        raise exceptions[random.randint(0, 2)]

    def __str__(self) -> str:
        return f"Event type: {self.__class__.__name__}"


class EventA(AbstractEvent):
    def run(self):
        super().run()


class EventB(AbstractEvent):
    def run(self):
        super().run()


class EventC(AbstractEvent):
    def run(self):
        super().run()


class EventD(AbstractEvent):
    def run(self):
        super().run()
