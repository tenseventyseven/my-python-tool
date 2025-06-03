"""Tests for CLI functionality."""

from typer.testing import CliRunner

from my_python_tool.cli import app

runner = CliRunner()


class TestCLI:
    """Test cases for CLI commands."""

    def test_version(self):
        """Test version command."""
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert "my-python-tool" in result.stdout

    def test_process_command(self):
        """Test process command."""
        result = runner.invoke(app, ["process", "test input"])
        assert result.exit_code == 0
        assert "Processed: test input" in result.stdout

    def test_process_verbose(self):
        """Test process command with verbose flag."""
        result = runner.invoke(app, ["process", "test input", "--verbose"])
        assert result.exit_code == 0
        assert "Processing: test input" in result.stdout
        assert "Processed: test input" in result.stdout

    def test_validate_valid_input(self):
        """Test validate command with valid input."""
        result = runner.invoke(app, ["validate", "valid input"])
        assert result.exit_code == 0
        assert "✓ Input is valid" in result.stdout

    def test_validate_invalid_input(self):
        result = runner.invoke(app, ["validate", ""])
        assert result.exit_code != 0
        assert "✗ Input is invalid" in result.stderr
