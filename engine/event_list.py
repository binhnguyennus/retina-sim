import enum


class EventType(enum.Enum):
    SEND_MESSAGE = 1
    SEND_FLIT = 2
    VC_ELECTION = 3


class EventList:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def push(self, event):
        self.queue.append(event)
        self.queue = sorted(self.queue, key=lambda ev: ev.time, reverse=True)

    def pull(self):
        if self.isEmpty():
            return None
        return self.queue.pop()

    def cancel(self, event):
        self.queue.remove(event)

    def __str__(self):
        return '\n'.join([str(i) for i in self.queue])
