from ply import yacc
from calculator.tokens import tokens
import calculator.eval_exceptions as eval_exceptions
from decimal import Decimal, getcontext
decimal_precision = 100
getcontext().prec = decimal_precision

precedence = (
    ('right', 'ROOT'),
    ('right', 'UMINUS', 'UPLUS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'JUSTINTDIVIDE'),
    ('left', 'MODULO'),
    ('right', 'POWER'),
    ('left', 'GROUP'),
    ('noassoc', 'PI', 'E', 'TAU'),
    ('left', 'NUMBER'),
    ('left', 'FLOAT'),
)
def p_expression_number(p):
    '''
    expression : NUMBER
               | NUMBER DOT NUMBER %prec FLOAT
    '''
    if len(p) == 2:
        p[0] = Decimal(p[1])
    else:
        p[0] = Decimal(str(p[1]) + '.' + str(p[3]))

def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression POWER expression
               | expression MODULO expression
               | expression JUSTINTDIVIDE expression
    '''
    match p[2]:
        case '+':
            p[0] = p[1] + p[3]
        case '-':
            p[0] = p[1] - p[3]
        case '*':
            p[0] = p[1] * p[3]
        case '/':
            if p[3] == 0:
                raise eval_exceptions.EvalException("Divisior may not be zero")
            p[0] = p[1] / p[3]
        case '^':
            p[0] = p[1] ** p[3]
        case '%':
            p[0] = p[1] % p[3]
        case '//':
            p[0] = p[1] // p[3]

def p_expression_unary(p):
    '''
    expression : MINUS expression %prec UMINUS
               | PLUS expression %prec UPLUS
    '''
    if p[1] == '-':
        p[0] = -p[2]
    elif p[1] == '+':
        p[0] = p[2]

def p_expression_group(p):
    '''
    expression : LPAREN expression RPAREN %prec GROUP
    '''
    p[0] = p[2]

def p_expression_root(p):
    '''
    expression : ROOT LPAREN expression RPAREN
               | expression ROOT LPAREN expression RPAREN
    '''
    
    if len(p) == 5:
        if p[3] < 0:
            raise eval_exceptions.EvalException("Unsupport i & Re numbers")
        p[0] = p[3] ** (Decimal('0.5'))
    else:
        if p[4] < 0:
            raise eval_exceptions.EvalException("Unsupport i & Re numbers")
        p[0] = p[4] ** (1/p[1])

def p_error(p):
    if p:
        raise eval_exceptions.SyntaxException(f"Syntax error at '{p.value}'")
    else:
        raise eval_exceptions.SyntaxException("Syntax error at EOF")

def p_constant(p):
    '''
    expression : PI
               | E
               | TAU
    '''
    match p[1]:
        case 'pi':
            p[0] = Decimal('3.1415926536')
        case 'e':
            p[0] = Decimal('2.7182818285')
        case 'tau':
            p[0] = Decimal('6.2831853072')

parser = yacc.yacc()