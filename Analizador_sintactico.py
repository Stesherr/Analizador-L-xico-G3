import ply.yacc as yacc
from Analizador_lexico import tokens
import Generador_log

def p_programa(p):
    '''programa : cuerpo
                | programa cuerpo
    '''
    
def p_cuerpo(p):
    '''cuerpo : arithmeticExpression
              | switchStatement
              | queueDeclaration
              | queueEnqueue
              | queueDequeue
              | arrowFunction
              | echo
              | fgets
    '''
# ESTRUCTURA SWITCH - KEVIN VALLE
def p_switchStatement(p):
    'switchStatement : SWITCH LPAREN value RPAREN LCURLY switchCases switchDefault RCURLY'

def p_switchDefault(p):
    'switchDefault : DEFAULT COLON arithmeticExpression'

def p_switchCase(p):
    'switchCase : CASE value COLON arithmeticExpression BREAK SEMICOLON'

def p_switchCases(p):
    '''switchCases : switchCase
                   | switchCases switchCase
    '''
# ESTRUCTURA SWITCH - KEVIN VALLE

# ESTRUCTURA COLA - KEVIN VALLE
def p_queueDeclaration(p):
    'queueDeclaration : ID EQUAL NEW QUEUE SEMICOLON'

def p_queueEnqueue(p):
    'queueEnqueue : ID OBJOP PUSH LPAREN value RPAREN SEMICOLON'

def p_queueDequeue(p):
    'queueDequeue : ID OBJOP POP SEMICOLON'
# ESTRUCTURA COLA - KEVIN VALLE

#  FUNCION FLECHA - KEVIN VALLE
def p_arrowFunction(p):
    'arrowFunction : FN LPAREN ID RPAREN FNARROW arrowBody SEMICOLON'

def p_arrowBody(p):
    '''arrowBody : FN LPAREN ID RPAREN FNARROW arrowBody
                 | cuerpo
    '''
#  FUNCION FLECHA - KEVIN VALLE

#  ECHO (IMPRIMIR valueES) - KEVIN VALLE
def p_echo(p):
    'echo : ECHO values SEMICOLON'

def p_values(p):
    '''values : value
               | values COMMA value
    '''
#  ECHO (IMPRIMIR valueES) - KEVIN VALLE

#  FGETS (INGRESAR value POR TECLADO) - KEVIN VALLE
def p_fgets(p):
    'fgets : ID EQUAL FGETS LPAREN STDIN RPAREN SEMICOLON'

def p_arithmeticExpression(p):
    'arithmeticExpression : value arithmeticOperator value'
#  FGETS (INGRESAR value POR TECLADO) - KEVIN VALLE

def p_value(p):
    '''value : ID 
             | INTEGER
             | FLOAT
             | STRING
             | BOOL
             | NULL
    '''

def p_arithmeticOperator(p):
    '''arithmeticOperator : PLUS
                          | MINUS 
                          | TIMES 
                          | DIVIDE
                          | MOD
                          | EXP
    '''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input! -> {}".format(p))


# Build the parser
parser = yacc.yacc()

algoritmos = Generador_log.algoritmos_3
resultados = {}

result = parser.parse(algoritmos['kevin_valle'])
print(result)
