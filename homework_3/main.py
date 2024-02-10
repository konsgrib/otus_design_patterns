import random
from event_fabric import (
    EventA,
    EventB,
    EventC,
    EventD,
)
from event_loop import EventLoop


def get_event():
    """
    Randomly generates events
    """
    random.seed()
    available_event_types = [EventA, EventB, EventC, EventD]
    eventtype_nr = random.randint(0, 3)
    event = available_event_types[eventtype_nr]

    return lambda: event().run(), event


event_loop = EventLoop()
number_of_commands = 20

# Fill the event queue with generated events
for i in range(number_of_commands):
    event = get_event()
    event_loop.add((event[0], event[1]))


event_loop.run()
