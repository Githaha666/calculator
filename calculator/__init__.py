from calculator.parser import parser
import calculator.test as test
__doc__ = """
Chinese.
欢迎使用计算器！我们支持：四则、指数、取余、整除、开根号、小数点、括号。
根号用法：root(x)表示x的平方根，nroot(x)表示x的n次方根。
建议在使用nroot(x)时把函数用括号包起来。2* 2root(16)=4。如果想要得到8的话，请使用2*(2root(16))。
注意！不支持虚数和复数！root(-1)是不被允许的！
单元测试在tests目录下。

English.
Welcome to the calculator! We support: arithmetic, exponent, modulo, integer division, square root, decimal point, parentheses.
Root usage: root(x) means the square root of x, nroot(x) means the n-th root of x.
It is recommended to use parentheses when using nroot(x). 2 * 2root(16) = 4. If you want to get 8, please use 2 * (2root(16)).
Note! We do not support complex numbers and complex numbers! root(-1) is not allowed!
Unit tests are in the tests directory.
"""

__version__ = "alpha0.0.0"

def calculate(expression):
    return parser.parse(expression)