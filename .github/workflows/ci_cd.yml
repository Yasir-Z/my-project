name: CI Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.9

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install flake8 black bandit mypy docker

      - name: Lint app.py with flake8
        run: |
          flake8 app.py

      - name: Check code formatting of app.py with black
        run: |
          black --check app.py

      - name: Static security analysis on app.py with bandit
        run: |
          bandit -r app.py

      - name: Type checking on app.py with mypy
        run: |
          mypy app.py

      - name: Run tests on app.py with pytest
        run: |
          pytest app.py --maxfail=1 --disable-warnings -q

  docker:
    runs-on: ubuntu-latest
    needs: test

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Build Docker image
        run: |
          docker build -t my-flask-app .

      - name: Run Docker container tests (pytest on app.py)
        run: |
          docker run --rm my-flask-app pytest app.py --maxfail=1 --disable-warnings -q

