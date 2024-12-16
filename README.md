# advent-of-code-2024

Having winter fun with Advent of Code 2024 ☃️


```shell
$ poetry run pre-commit run -av
black....................................................................Passed
- hook id: black
- duration: 0.36s

All done! ✨ 🍰 ✨
33 files left unchanged.

flake8...................................................................Passed
- hook id: flake8
- duration: 0.31s
mypy.....................................................................Passed
- hook id: mypy
- duration: 2.15s

Success: no issues found in 33 source files

pytest...................................................................Passed
- hook id: pytest
- duration: 1.16s

============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 55 items / 15 deselected / 40 selected                               

tests/test_p01.py ..                                                     [  5%]
tests/test_p02.py ..                                                     [ 10%]
tests/test_p03.py ..                                                     [ 15%]
tests/test_p04.py ..                                                     [ 20%]
tests/test_p05.py ..                                                     [ 25%]
tests/test_p06.py ....                                                   [ 35%]
tests/test_p07.py ..                                                     [ 40%]
tests/test_p08.py ..                                                     [ 45%]
tests/test_p09.py ....                                                   [ 55%]
tests/test_p10.py ..                                                     [ 60%]
tests/test_p11.py ..                                                     [ 65%]
tests/test_p12.py ........                                               [ 85%]
tests/test_p13.py .                                                      [ 87%]
tests/test_p14.py .                                                      [ 90%]
tests/test_p15.py ....                                                   [100%]

====================== 40 passed, 15 deselected in 0.26s =======================

performance..............................................................Passed
- hook id: performance
- duration: 17.26s

============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 55 items / 40 deselected / 15 selected                               

tests/test_performance.py ...............
────────────────────────────────── Run Times ───────────────────────────────────
p01  0.04
p02  0.05
p03  0.04
p04 ▇ 0.08
p05  0.04
p06 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 6.71
p07 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 8.71
p08  0.04
p09 ▇ 0.10
p10  0.06
p11 ▇▇ 0.24
p12 ▇▇ 0.21
p13  0.04
p14  0.04
p15 ▇ 0.12


====================== 15 passed, 40 deselected in 16.61s ======================
```
