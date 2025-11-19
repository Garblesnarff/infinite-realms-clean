# Contributing to Infinite Realms

Thank you for your interest in contributing to Infinite Realms! This document provides guidelines and information for contributors.

## Ways to Contribute

- 🐛 Report bugs and issues
- 💡 Suggest new features or improvements
- 📝 Improve documentation
- 🔧 Submit bug fixes
- ✨ Add new features
- 🎨 Improve output formatting
- 🤖 Create new custom tools
- 📚 Share example campaigns

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/infinite-realms-clean.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit: `git commit -m "Description of changes"`
7. Push: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Development Setup

```bash
# Clone and setup
git clone <your-fork-url>
cd infinite-realms-clean
python -m venv venv
source venv/bin/activate

# Install with dev dependencies
pip install -e ".[dev]"

# Setup environment
cp .env.example .env
# Add your API keys to .env
```

## Code Style

We use:
- **Black** for code formatting
- **Ruff** for linting
- **MyPy** for type checking

Run before committing:
```bash
black src/ tests/
ruff check src/ tests/
mypy src/
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test
pytest tests/test_tools.py::test_consistency_checker
```

## Pull Request Guidelines

### Good PRs

- ✅ Focused on a single feature/fix
- ✅ Include tests for new functionality
- ✅ Update documentation as needed
- ✅ Follow existing code style
- ✅ Clear commit messages
- ✅ Reference related issues

### PR Description Should Include

1. **What**: What does this PR do?
2. **Why**: Why is this change needed?
3. **How**: How does it work?
4. **Testing**: How was it tested?

## Adding New Features

### New Custom Tools

1. Create file in `src/tools/your_tool.py`
2. Inherit from `BaseTool`
3. Implement `_run()` method
4. Add comprehensive docstrings
5. Add tests in `tests/test_tools.py`
6. Update `src/tools/__init__.py`
7. Document in `docs/tools.md`

Example:
```python
from crewai_tools import BaseTool
from pydantic import BaseModel, Field

class YourToolInput(BaseModel):
    input: str = Field(..., description="Input description")

class YourTool(BaseTool):
    name: str = "Your Tool"
    description: str = "What your tool does"
    args_schema: Type[BaseModel] = YourToolInput

    def _run(self, input: str) -> str:
        # Implementation
        return result
```

### New Output Formatters

1. Create file in `src/formatters/your_formatter.py`
2. Implement `format_full_bible()` method
3. Implement `save_to_file()` method
4. Add tests
5. Update `src/formatters/__init__.py`
6. Add CLI option in `src/main.py`

### New Agent Types

1. Add to `src/config/agents.yaml`
2. Define role, goal, backstory
3. Create tasks in `src/config/tasks.yaml`
4. Update crew initialization if needed
5. Document the agent's purpose

## Documentation

Update documentation when you:
- Add new features
- Change existing functionality
- Add configuration options
- Create new tools or formatters

Documentation files:
- `README.md` - Overview and quick start
- `docs/quick_start.md` - Installation and basic usage
- `docs/best_practices.md` - Tips and guidelines
- `docs/architecture.md` - System design
- `docs/tools.md` - Custom tools reference
- `docs/api.md` - API reference

## Commit Message Guidelines

Use conventional commits format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
```
feat(tools): add spell validator tool
fix(formatter): handle missing NPC data gracefully
docs(readme): update installation instructions
```

## Issue Guidelines

### Reporting Bugs

Include:
- Clear description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- System information (OS, Python version)
- Relevant logs or error messages
- Campaign config (if applicable)

### Suggesting Features

Include:
- Clear description of the feature
- Use cases and benefits
- Proposed implementation (if you have ideas)
- Examples of similar features elsewhere

## Code Review Process

1. Maintainer reviews PR
2. Feedback provided (if needed)
3. You address feedback
4. Approval and merge

We aim to review PRs within 1 week.

## Community Guidelines

- Be respectful and inclusive
- Help others in issues and discussions
- Give constructive feedback
- Credit others' work
- Follow the Code of Conduct

## Questions?

- Open an issue for bugs or feature requests
- Start a discussion for general questions
- Tag maintainers if you need help

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for making Infinite Realms better! 🎲⚔️🐉
