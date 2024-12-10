# advent-of-code-2024

Having winter fun with Advent of Code 2024 ☃️


```shell
$ poetry run pre-commit run -av
black....................................................................Passed
- hook id: black
- duration: 0.3s

All done! ✨ 🍰 ✨
21 files left unchanged.

flake8...................................................................Passed
- hook id: flake8
- duration: 0.28s
mypy.....................................................................Passed
- hook id: mypy
- duration: 2.04s

Success: no issues found in 21 source files

pytest...................................................................Passed
- hook id: pytest
- duration: 1.09s

============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 31 items / 9 deselected / 22 selected                                

tests/test_p01.py ..                                                     [  9%]
tests/test_p02.py ..                                                     [ 18%]
tests/test_p03.py ..                                                     [ 27%]
tests/test_p04.py ..                                                     [ 36%]
tests/test_p05.py ..                                                     [ 45%]
tests/test_p06.py ....                                                   [ 63%]
tests/test_p07.py ..                                                     [ 72%]
tests/test_p08.py ..                                                     [ 81%]
tests/test_p09.py ....                                                   [100%]

======================= 22 passed, 9 deselected in 0.21s =======================

performance..............................................................Passed
- hook id: performance
- duration: 16.45s

============================= test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/runner/work/advent-of-code-2024/advent-of-code-2024
configfile: pytest.ini
collecting ... 
collected 31 items / 22 deselected / 9 selected                                

tests/test_performance.py .........
────────────────────────────────── Run Times ───────────────────────────────────
p01  0.04
p02  0.05
p03  0.04
p04 ▇ 0.08
p05  0.04
p06 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 6.69
p07 ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 8.64
p08  0.04
p09 ▇ 0.09


====================== 9 passed, 22 deselected in 15.79s =======================
```
