# Python Template

Simple Python project template with **Poetry** and **Pytest**, configured for **SonarQube** analysis.

## Useful Commands (Poetry)

- `pip install -r requirements.txt` - Install Poetry
- `poetry install` - Install dependencies
- `poetry run pytest` - Run tests
- `poetry run hello` - Run the hello script

## Other Commands

To generate a distribution package, you can use the provided `dist.sh` script. This script uses **PyInstaller** to create a standalone executable of the project inside the `dist/` directory.
