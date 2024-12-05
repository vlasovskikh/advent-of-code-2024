# advent-of-code-2024

Having winter fun with Advent of Code 2024 ☃️


```shell
$ poetry run pre-commit run -av
black....................................................................Passed
- hook id: black
- duration: 0.26s

All done! ✨ 🍰 ✨
13 files left unchanged.

flake8...................................................................Passed
- hook id: flake8
- duration: 0.24s
mypy.....................................................................Passed
- hook id: mypy
- duration: 1.56s

Success: no issues found in 13 source files

pytest...................................................................Passed
- hook id: pytest
- duration: 1.02s

============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 15 items / 5 deselected / 10 selected                                

tests/test_p01.py ..                                                     [ 20%]
tests/test_p02.py ..                                                     [ 40%]
tests/test_p03.py ..                                                     [ 60%]
tests/test_p04.py ..                                                     [ 80%]
tests/test_p05.py ..                                                     [100%]

======================= 10 passed, 5 deselected in 0.15s =======================

performance..............................................................Passed
- hook id: performance
- duration: 1.0s

============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 15 items / 10 deselected / 5 selected                                

tests/test_performance.py .....
────────────────────────────────── Run Times ───────────────────────────────────
p01 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.04
p02 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.05
p03 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.04
p04 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.13
p05 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 0.05


======================= 5 passed, 10 deselected in 0.36s =======================
```
