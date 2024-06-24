import ply.yacc as yacc
from Analizador_lexico import tokens
import Generador_log

def p_programa(p):
    '''programa : cuerpo
                | programa cuerpo
    '''

def p_cuerpo(p):
    '''cuerpo : arithmeticExpression
              | if_elseStatement
              | forStatement
              | switchStatement
              | queueDeclaration
              | queueEnqueue
              | queueDequeue
              | defineFunction
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

# ESTRUCTURA IF/ELSE - STEFANO SUAREZ
def p_if_elseStatement(p):
    '''if_elseStatement : IF LPAREN comparingValue RPAREN LCURLY ifStatementBody RCURLY ELSE ifStatementBody
                        | IF LPAREN comparingValue RPAREN LCURLY ifStatementBody'''

def p_ifStatementBody(p):
    '''ifStatementBody : cuerpo
                       | ifStatementBody cuerpo'''

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

# DEFINE FUNCTION - LUIS QUEZADA
def p_defineFunction(p):
    '''defineFunction : FUNCTION ID LPAREN arguments RPAREN LCURLY cuerpo RCURLY
                    | FUNCTION ID LPAREN RPAREN LCURLY cuerpo RCURLY'''

# ARGUMENTS - LUIS QUEZADA
def p_arguments(p):
    '''arguments : ID
                | ID COMMA arguments'''

#  FUNCION FLECHA - KEVIN VALLE
def p_arrowFunction(p):
    'arrowFunction : FN LPAREN ID RPAREN FNARROW arrowBody SEMICOLON'

def p_arrowBody(p):
    '''arrowBody : FN LPAREN ID RPAREN FNARROW arrowBody
                 | cuerpo
    '''
#  FUNCION FLECHA - KEVIN VALLE

#  ECHO (IMPRIMIR values) - KEVIN VALLE
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
    print("Error en -> {}".format(p))


# Build the parser
parser = yacc.yacc()

algoritmos = Generador_log.algoritmos_3
resultados = {}

result = parser.parse(algoritmos['stefano_suarez'])
print(result)
'''
for key, value in algoritmos.items():
    result = parser.parse(value)

print(resultados['luis_quezada'])
'''