"""Tests for core functionality."""

import pytest

from my_python_tool.core import MyPythonTool


class TestMyTool:
    """Test cases for MyPythonTool class."""

    def test_init_default(self):
        """Test initialization with default config."""
        tool = MyPythonTool()
        assert tool.config == {}

    def test_init_with_config(self):
        """Test initialization with custom config."""
        config = {"key": "value"}
        tool = MyPythonTool(config)
        assert tool.config == config

    def test_process(self):
        """Test process method."""
        tool = MyPythonTool()
        result = tool.process("test input")
        assert result == "Processed: test input"

    @pytest.mark.parametrize(
        "input_data,expected",
        [
            ("valid input", True),
            ("", False),
            ("   ", False),
            ("  text  ", True),
        ],
    )
    def test_validate_input(self, input_data, expected):
        """Test validate_input method with various inputs."""
        tool = MyPythonTool()
        result = tool.validate_input(input_data)
        assert result == expected
