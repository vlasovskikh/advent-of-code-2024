# advent-of-code-2024

Having winter fun with Advent of Code 2024 ☃️


```shell
$ poetry run pre-commit run -av
black....................................................................Passed
- hook id: black
- duration: 0.31s

All done! ✨ 🍰 ✨
27 files left unchanged.

flake8...................................................................Passed
- hook id: flake8
- duration: 0.29s
mypy.....................................................................Passed
- hook id: mypy
- duration: 2.1s

Success: no issues found in 27 source files

pytest...................................................................Passed
- hook id: pytest
- duration: 1.1s

============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 46 items / 12 deselected / 34 selected                               

tests/test_p01.py ..                                                     [  5%]
tests/test_p02.py ..                                                     [ 11%]
tests/test_p03.py ..                                                     [ 17%]
tests/test_p04.py ..                                                     [ 23%]
tests/test_p05.py ..                                                     [ 29%]
tests/test_p06.py ....                                                   [ 41%]
tests/test_p07.py ..                                                     [ 47%]
tests/test_p08.py ..                                                     [ 52%]
tests/test_p09.py ....                                                   [ 64%]
tests/test_p10.py ..                                                     [ 70%]
tests/test_p11.py ..                                                     [ 76%]
tests/test_p12.py ........                                               [100%]

====================== 34 passed, 12 deselected in 0.23s =======================

performance..............................................................Passed
- hook id: performance
- duration: 16.97s

============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 46 items / 34 deselected / 12 selected                               

tests/test_performance.py ............
────────────────────────────────── Run Times ───────────────────────────────────
p01  0.04
p02  0.05
p03  0.04
p04 ▇ 0.07
p05  0.04
p06 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 6.63
p07 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 8.74
p08  0.04
p09 ▇ 0.10
p10  0.05
p11 ▇▇ 0.24
p12 ▇▇ 0.20


====================== 12 passed, 34 deselected in 16.33s ======================
```
