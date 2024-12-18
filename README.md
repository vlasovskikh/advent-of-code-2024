# advent-of-code-2024

Having winter fun with Advent of Code 2024 ☃️


```shell
$ poetry run pre-commit run -av
black....................................................................Passed
- hook id: black
- duration: 0.38s

All done! ✨ 🍰 ✨
39 files left unchanged.

flake8...................................................................Passed
- hook id: flake8
- duration: 0.33s
mypy.....................................................................Passed
- hook id: mypy
- duration: 2.23s

Success: no issues found in 39 source files

pytest...................................................................Passed
- hook id: pytest
- duration: 1.14s

============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 64 items / 18 deselected / 46 selected                               

tests/test_p01.py ..                                                     [  4%]
tests/test_p02.py ..                                                     [  8%]
tests/test_p03.py ..                                                     [ 13%]
tests/test_p04.py ..                                                     [ 17%]
tests/test_p05.py ..                                                     [ 21%]
tests/test_p06.py ....                                                   [ 30%]
tests/test_p07.py ..                                                     [ 34%]
tests/test_p08.py ..                                                     [ 39%]
tests/test_p09.py ....                                                   [ 47%]
tests/test_p10.py ..                                                     [ 52%]
tests/test_p11.py ..                                                     [ 56%]
tests/test_p12.py ........                                               [ 73%]
tests/test_p13.py .                                                      [ 76%]
tests/test_p14.py .                                                      [ 78%]
tests/test_p15.py ....                                                   [ 86%]
tests/test_p16.py ...                                                    [ 93%]
tests/test_p17.py .                                                      [ 95%]
tests/test_p18.py ..                                                     [100%]

====================== 46 passed, 18 deselected in 0.28s =======================

performance..............................................................Passed
- hook id: performance
- duration: 16.54s

============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 64 items / 46 deselected / 18 selected                               

tests/test_performance.py ..................
────────────────────────────────── Run Times ───────────────────────────────────
p01  0.04
p02  0.05
p03  0.04
p04 ▇ 0.07
p05  0.05
p06 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 5.76
p07 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 8.52
p08  0.04
p09 ▇ 0.10
p10  0.05
p11 ▇▇ 0.24
p12 ▇▇ 0.20
p13  0.04
p14  0.04
p15 ▇ 0.12
p16 ▇▇ 0.23
p17  0.04
p18 ▇ 0.16


====================== 18 passed, 46 deselected in 15.90s ======================
```
