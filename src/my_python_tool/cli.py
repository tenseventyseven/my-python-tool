"""Command-line interface for my-python-tool."""

from pathlib import Path
from typing import Annotated, Optional

import typer

from . import __version__
from .core import MyPythonTool

app = typer.Typer(
    name="my-python-tool",
    help="A simple tool with CLI interface",
    add_completion=False,
)


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        typer.echo(f"my-python-tool {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            callback=version_callback,
            is_eager=True,
            help="Show version and exit",
        ),
    ] = None,
) -> None:
    """Main callback for global options."""
    pass


@app.command()
def process(
    input_text: Annotated[str, typer.Argument(help="Text to process")],
    output_file: Annotated[
        Optional[Path],
        typer.Option("--output", "-o", help="Output file path (optional)"),
    ] = None,
    verbose: Annotated[
        bool, typer.Option("--verbose", "-v", help="Enable verbose output")
    ] = False,
) -> None:
    """Process input text and optionally save to file.

    Args:
        input_text: The text to process
        output_file: Optional output file path
        verbose: Enable verbose logging
    """
    tool = MyPythonTool()

    if not tool.validate_input(input_text):
        typer.echo("Error: Invalid input text", err=True)
        raise typer.Exit(1)

    if verbose:
        typer.echo(f"Processing: {input_text}")

    result = tool.process(input_text)

    if output_file:
        output_file.write_text(result)
        typer.echo(f"Output written to: {output_file}")
    else:
        typer.echo(result)


@app.command()
def validate(
    input_text: Annotated[str, typer.Argument(help="Text to validate")],
) -> None:
    """Validate input text.

    Args:
        input_text: The text to validate
    """
    tool = MyPythonTool()
    is_valid = tool.validate_input(input_text)

    if is_valid:
        typer.echo("✓ Input is valid")
    else:
        typer.echo("✗ Input is invalid", err=True)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
