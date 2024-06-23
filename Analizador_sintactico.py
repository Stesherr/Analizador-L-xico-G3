import ply.yacc as yacc
from Analizador_lexico import tokens

def p_cuerpo(p):
    '''cuerpo : arithmeticExpression
              | forStatement
              | switchStatement
              | queueDeclaration
              | queueEnqueue
              | queueDequeue
              | arrowFunction
              | echo
              | fgets
              | stackDeclaration
              | stackPush
              | stackPop
              | line
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

# ESTRUCTURA FOR - LUIS QUEZADA
def p_forStatement(p):
    'forStatement : FOR LPAREN forStatementCondition RPAREN LCURLY forStatementBody RCURLY'

def p_forStatementCondition(p):
    '''forStatementCondition :  SEMICOLON SEMICOLON 
                            |  variableAsignation SEMICOLON SEMICOLON variableAsignation
                            |  variableAsignation SEMICOLON comparingValue SEMICOLON variableAsignation'''

def p_forStatementBody(p):
    '''forStatementBody : cuerpo 
                        | forStatementBody cuerpo'''
# ESTRUCTURA FOR - LUIS QUEZADA

# ESTRUCTURA COLA - STEFANO SUAREZ
def p_stackDeclaration(p):
    'stackDeclaration : ID EQUAL NEW STACK SEMICOLON'

def p_stackPush(p):
    'stackPush : ID OBJOP PUSH LPAREN value RPAREN SEMICOLON'

def p_stackPop(p):
    'stackPop : ID OBJOP POP SEMICOLON'

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

# LINE - LUIS QUEZADA
def p_line(p):
    '''line : variableAsignation SEMICOLON'''
    
# VARIABLE ASIGNATION - LUIS QUEZADA
def p_variableAsignation(p):
    '''variableAsignation : ID EQUAL value
                            | ID EQUAL arithmeticExpression
    '''

# COMPARING SIGN - LUIS QUEZADA
def p_comparingSign(p):
    '''comparingSign : IS_EQUAL
                        | IDENTICAL
                        | NOTEQUAL
                        | LESSTHAN
                        | GREATERTHAN
                        | LESSEQUALTHAN
                        | GREATEREQUALTHAN
    '''

# COMPARING VALUES - LUIS QUEZADA
def p_comparingValue(p):
    'comparingValue : value comparingSign value'

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('lp > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
