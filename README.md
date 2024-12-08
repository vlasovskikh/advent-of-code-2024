# advent-of-code-2024

Having winter fun with Advent of Code 2024 ☃️


```shell
$ poetry run pre-commit run -av
black....................................................................Passed
- hook id: black
- duration: 0.27s
All done! ✨ 🍰 ✨
17 files left unchanged.
flake8...................................................................Passed
- hook id: flake8
- duration: 0.25s
mypy.....................................................................Passed
- hook id: mypy
- duration: 1.91s
Success: no issues found in 17 source files
pytest...................................................................Passed
- hook id: pytest
- duration: 1.04s
============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 23 items / 7 deselected / 16 selected                                
tests/test_p01.py ..                                                     [ 12%]
tests/test_p02.py ..                                                     [ 25%]
tests/test_p03.py ..                                                     [ 37%]
tests/test_p04.py ..                                                     [ 50%]
tests/test_p05.py ..                                                     [ 62%]
tests/test_p06.py ....                                                   [ 87%]
tests/test_p07.py ..                                                     [100%]
======================= 16 passed, 7 deselected in 0.18s =======================
performance..............................................................Passed
- hook id: performance
- duration: 21.85s
============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 23 items / 16 deselected / 7 selected                                
tests/test_performance.py .......
────────────────────────────────── Run Times ───────────────────────────────────
p01  0.04
p02  0.05
p03  0.04
p04 ▇ 0.12
p05  0.04
p06 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 12.19
p07 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 8.68
====================== 7 passed, 16 deselected in 21.22s =======================
```
