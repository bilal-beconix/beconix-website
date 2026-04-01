# Tests

This folder contains all test files for the Beconix website.

## Test Files

- **test_fixed_app.py** - Code structure and Flask app validation tests
- **test_logo.py** - Static file serving and logo display tests
- **test_mobile.py** - Mobile responsiveness tests (iPhone, iPad, Desktop)
- **test_webhook.py** - Make.com webhook integration tests

## Running Tests

To run all tests:

```bash
# Activate virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run individual tests
python tests/test_fixed_app.py
python tests/test_logo.py
python tests/test_mobile.py
python tests/test_webhook.py
```

## Test Coverage

- ✅ 22+ unit tests covering Flask routing
- ✅ Form submission and validation
- ✅ Webhook integration
- ✅ Static file serving
- ✅ Mobile responsiveness (375px - 430px)
- ✅ Favicon and logo display

All tests should pass before deployment.
