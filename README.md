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
coverage html --omit="*/test*" -d test/coverage
```
writes report to tests/coverage/index.html
