# didacTicTacToe

## Summary
Boardgame TicTacToe implemented in python to get familiar with the language

## How to run
Run standard TicTacToe game on 3x3 tiles board:
```bash
python run_standard_tictactoe.py
```

Run TicTacToe game on 9x9 tiles board with a row of 5 to win the game:
```bash
python run_five_wins.py
```

## Tests
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
rm -rf test/cov_report_
pytest --cov --cov-config=test/.coveragerc --cov-report=html:test/cov_report
```
writes report to
```bash
firefox test/cov_report/index.html
```

