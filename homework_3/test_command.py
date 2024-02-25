
import pytest
from unittest.mock import MagicMock
from datetime import datetime
from unittest.mock import MagicMock, mock_open, patch

# Assuming the classes are in a file named 'commands.py'
from command import SpaceshipCommand, LoggerCommand, RepeaterCommand, DoubleRepeatedCommand

def test_spaceship_command_execute():
    spaceship = MagicMock()
    command = SpaceshipCommand(spaceship, "move")
    command.execute()
    spaceship.move.assert_called_once()

def test_spaceship_command_execute_rotation():
    spaceship = MagicMock()
    command = SpaceshipCommand(spaceship, "rotate", 180)
    command.execute()
    spaceship.rotate.assert_called_once_with(180)

def test_spaceship_command_execute_invalid():
    spaceship = MagicMock()
    command = SpaceshipCommand(spaceship, "invalid")
    with pytest.raises(ValueError):
        command.execute()

from unittest.mock import patch

def test_logger_command_execute():
    cmd = MagicMock()
    error = ValueError("Invalid action")
    command = LoggerCommand(cmd, error)
    with patch("builtins.open", mock_open()) as mock_file:
        command.execute()

    mock_file().write.assert_called_once()

def test_repeater_command_execute():
    cmd = MagicMock()
    command = RepeaterCommand(cmd)
    command.execute()
    cmd.execute.assert_called_once()

def test_double_repeated_command_execute():
    cmd = MagicMock()
    command = DoubleRepeatedCommand(cmd)
    command.execute()
    cmd.execute.assert_called_once()
