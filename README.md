# didacTicTacToe

## Summary
Boardgame TicTacToe implemented in python to get familiar with the language

## How to run
Run standard TicTacToe game on 3x3 tiles board:
```bash
python run_standard_tictactoe.py
```

Run all tests (see directory `test/`):
```bash
pytest
```

Watch two scripted players play games:
```bash
pytest test/test_smoketest_tictactoe.py -s
```

Analyse test coverage:
```bash
rm -rf test/coverage
coverage html --omit="*/test*" -d test/coverage
```
writes report to `test/coverage/index.html`

or via pytest-cov plugin
```bash
rm -rf test/coverage_report_cov
pytest --cov --cov-report=html:test/coverage_report_cov
```
writes report to `test/coverage_report_cov/index.html`, but includes imported libraries and test files themselves

