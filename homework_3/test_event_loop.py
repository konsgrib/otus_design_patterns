import pytest

from unittest.mock import MagicMock
from event_loop import EventLoop

from command import (LoggerCommand, RepeaterCommand, DoubleRepeatedCommand,SpaceshipCommand, )

def test_add():
    event_loop = EventLoop()
    cmd = MagicMock()
    event_loop.add(cmd)
    assert len(event_loop.ready) == 1

def test_run_no_exception():
    event_loop = EventLoop()
    cmd = MagicMock()
    event_loop.add(cmd)
    event_loop.run()
    cmd.execute.assert_called_once()

def test_run_with_exceptions():
    event_loop = EventLoop()
    cmd = MagicMock()
    cmd.execute = MagicMock()
    cmd.execute.side_effect = Exception()
    event_loop.add(cmd)
    event_loop.run()
    if event_loop.ready:
        assert isinstance(event_loop.ready[0], DoubleRepeatedCommand)
    cmd.execute.assert_called()
    