# MLops-RTG6-CI

Small demo repository showing a minimal Python app, unit tests, and GitHub Actions CI.

Concept
- Simple Streamlit UI (`app.py`) that computes the square, cube, and fifth power of a number.
- Unit tests (`_test.py`) verify the math functions; CI runs those tests on push/PR to `main`.

Files
- `_test.py`: pytest unit tests for `square`, `cube`, and `fifth_power`.
- `app.py`: Streamlit app (Power Calculator) that computes and shows results.
- `.github/workflows/ci.yaml`: GitHub Actions workflow that installs test deps and runs `pytest`.

Run locally
- Install dependencies:

```bash
python -m pip install --upgrade pip
pip install pytest streamlit
```

- Run the Streamlit app (opens a local web UI):

```bash
python app.py
# or: streamlit run app.py
```

- Run tests:

```bash
pytest _test.py -q
```

CI notes
- The CI workflow runs pytest on `main` and on pull requests. A recent failure was caused by installing `streamlit` in CI; it was removed to keep CI focused on unit tests.

Next steps / suggestions
- Add a `requirements.txt` to pin dependencies.
- Cache pip installs in CI to speed runs.
- Conditionally install UI deps only when needed.

License
- See `LICENSE`.

Contact
- Open issues or PRs on the repository for improvements.