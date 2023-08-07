# didacTicTacToe

## Summary
Boardgame TicTacToe implemented in ``python`` to get familiar with the language

## How to run

### Standard TicTacToe
Run standard TicTacToe game on 3x3 tiles board:


**Rules:**
https://en.wikipedia.org/wiki/Tic-tac-toe
```bash
python run_standard_tictactoe.py
```

### Gomoku (TicTacToe with 5 in a row to win, larger Board)
Run TicTacToe game on 15x15 tiles board with a row of 5 to win the game:

**Rules:**
https://en.wikipedia.org/wiki/Gomoku
```bash
python run_five_wins.py
```
### Four in a row including Gravity
Run Four Wins game with gravity on 7x6 tiles board with a row of 4 to win the game.
Only tiles, that are the lowest empty one in their column can be claimed within a move.

**Rules:**
https://en.wikipedia.org/wiki/Connect_Four
```bash
python run_four_wins_gravity.py
```

## Tests

### Run Tests
Run all tests (see directory `test/`):
```bash
pytest
```

Watch two scripted players play games:
```bash
pytest test/test_smoketest_tictactoe.py -s
```

### Analyze Test Coverage
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

