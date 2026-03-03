from ply import lex
import calculator.eval_exceptions as eval_exceptions
from decimal import Decimal

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'POWER',
    'MODULO',
    'DOT',
    'JUSTINTDIVIDE',
    'ROOT',
    'PI',
    'E',
    'TAU'
)

t_PI = r'pi'
t_E = r'e'
t_TAU = r'tau'
t_ROOT = r'root'
t_JUSTINTDIVIDE = r'//'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_POWER = r'\^'
t_DOT = r'\.'
t_MODULO = r'%'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    raise eval_exceptions.TokensException(f"Illegal character {t.value[0]}")

t_ignore = ' \t'

lexer = lex.lex()