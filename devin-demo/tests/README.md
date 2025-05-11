# Tests for devin-hello-function

This directory contains tests for the `devin-hello-function` Cloud Function.

## Structure

- `test_main.py`: Tests for the `hello_world` function in `function/main.py`
- `conftest.py`: Configuration for pytest
- `requirements.txt`: Test dependencies

## Running Tests

To run the tests:

```bash
# Install test dependencies
pip install -r tests/requirements.txt

# Run tests with pytest
python -m pytest tests/

# Run tests with coverage
python -m pytest tests/ --cov=function
```

## Test Cases

1. `test_hello_world_logging`: Verifies that the function logs the expected message
2. `test_hello_world_return_value`: Verifies that the function returns the expected string
