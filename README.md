# My Python Tool

A simple tool with CLI interface built with modern Python practices. Initially "vibe"-coded from Claude Sonnet 4 on 20250603 as a best practices scaffold then audited and trimmed the fat.

Initial prompt:

```txt
Give me a modern Python library structure with CLI frontend using:

Python 3.12+
uv for dependency management
ruff for linting/formatting
typer for CLI
Minimal configuration preferring built-in defaults
```

## Installation

Using uv (recommended):

```bash
uv add git+ssh://git@github.com/tenseventyseven/my-python-tool.git
```

## Usage

### CLI Commands

Process text:

```bash
my-python-tool process "your text here"
```

Process with output file:

```bash
my-python-tool process "your text" --output result.txt
```

Validate input:

```bash
my-python-tool validate "your text"
```

### Python API

```python
from my_tool import MyTool

tool = MyTool()
result = tool.process("your input")
print(result)
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/my-python-tool.git
cd my-python-tool

# Install with development dependencies
uv sync --dev
```

### Running Tests

```bash
uv run pytest
```

### Code Quality

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check

# Fix linting issues
uv run ruff check --fix
```

## License

MIT
