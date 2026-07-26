PYTHONPATH=src python3 -m unittest discover tests
flake8 src tests || true
