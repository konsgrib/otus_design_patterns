from collections import deque
from exception_handler import ExceptionHandler
from command import LoggerCommand, RepeaterCommand, DoubleRepeatedCommand


class EventLoop:
    def __init__(self):
        self.ready = deque()

    def add(self, cmd):
        self.ready.append(cmd)

    def run(self):
        while self.ready:
            print("QUEUE: ", self.ready)
            cmd = self.ready.popleft()
            try:
                cmd.execute()
            except Exception as e:
                ExceptionHandler(cmd, e).handle()
                if isinstance(cmd, DoubleRepeatedCommand):
                    print("Double Repeated Command failed writing to the log...")
                    logger_cmd = LoggerCommand(cmd, e)
                    self.add(logger_cmd)
                elif isinstance(cmd, RepeaterCommand):
                    print("Repeated Command failed, creating double...")
                    double_repeated_cmd = DoubleRepeatedCommand(cmd)
                    self.add(double_repeated_cmd)
                else:
                    print("Creating repeater for the command failed first time...")
                    repeater_cmd = RepeaterCommand(cmd)
                    self.add(repeater_cmd)


