import ply.yacc as yacc
from Analizador_lexico import tokens
import Generador_log

variables = {}

def p_programa(p):
    '''programa : cuerpo
                | programa cuerpo
    '''

def p_cuerpo(p):
    '''cuerpo : arithmeticExpression
              | if_elseStatement
              | forStatement
              | switchStatement
              | arrayAsignation
              | queueDeclaration
              | queueEnqueue
              | queueDequeue
              | defineFunction
              | anonymousFunction
              | arrowFunction
              | echo
              | fgets
              | stackDeclaration
              | stackPush
              | stackPop
              | line
              | print
              | logicalCondition
              | OPEN_TAG
              | CLOSE_TAG
    '''
# ESTRUCTURA SWITCH - KEVIN VALLE
def p_switchStatement(p):
    'switchStatement : SWITCH LPAREN value RPAREN LCURLY switchCases switchDefault RCURLY'


def p_switchDefault(p):
    'switchDefault : DEFAULT COLON programa'

def p_switchCase(p):
    'switchCase : CASE value COLON programa BREAK SEMICOLON'

def p_switchCases(p):
    '''switchCases : switchCase
                   | switchCases switchCase
    '''

# ESTRUCTURA IF/ELSE - STEFANO SUAREZ
def p_if_elseStatement(p):
    '''if_elseStatement : IF LPAREN logicalCondition RPAREN LCURLY ifStatementBody RCURLY ELSE ifStatementBody
                        | IF LPAREN logicalCondition RPAREN LCURLY ifStatementBody'''

def p_ifStatementBody(p):
    '''ifStatementBody : cuerpo
                       | cuerpo CONTINUE SEMICOLON
                       | ifStatementBody cuerpo
                       '''

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

#ESTRUCTURA ARREGLO - LUIS QUEZADA
def p_arrayAsignation(p):
    'arrayAsignation : ID EQUAL arrayDeclaration SEMICOLON'

def p_arrayDeclaration(p):
    ''' arrayDeclaration : ARRAY arraysValues RPAREN
                        | LSQUARE arraysValues RSQUARE
                        | arrayValue '''

def p_arraysValues(p):
    ''' arraysValues : arrayValue 
                    | arraysValues COMMA arrayValue'''

def p_arrayValue(p):
    '''arrayValue : ARRAY values RPAREN
                    | LSQUARE values RSQUARE'''

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

# DEFINE FUNCTION - LUIS QUEZADA
def p_defineFunction(p):
    '''defineFunction : FUNCTION ID LPAREN arguments RPAREN LCURLY cuerpo RCURLY
                    | FUNCTION ID LPAREN RPAREN LCURLY cuerpo RCURLY'''

# ARGUMENTS - LUIS QUEZADA
def p_arguments(p):
    '''arguments : ID
                | ID COMMA arguments'''
    
# FUNCION ANONIMA - STEFANO SUAREZ
def p_anonymousFunction(p):
    '''anonymousFunction : FUNCTION LPAREN RPAREN LCURLY cuerpo RCURLY 
                         | FUNCTION LPAREN arguments RPAREN LCURLY cuerpo RCURLY'''

#  FUNCION FLECHA - KEVIN VALLE
def p_arrowFunction(p):
    'arrowFunction : FN LPAREN ID RPAREN FNARROW arrowBody SEMICOLON'

def p_arrowBody(p):
    '''arrowBody : FN LPAREN ID RPAREN FNARROW arrowBody
                 | cuerpo
    '''

#  ECHO (IMPRIMIR values), PRINT - KEVIN VALLE
def p_echo(p):
    'echo : ECHO values SEMICOLON'

def p_print(p):
    '''
    print : PRINT LPAREN values RPAREN SEMICOLON
          | PRINT value SEMICOLON
    '''

def p_values(p):
    '''values : value
              | values COMMA value
    '''

#  FGETS (INGRESAR value POR TECLADO) - KEVIN VALLE
def p_fgets(p):
    'fgets : ID EQUAL FGETS LPAREN STDIN RPAREN SEMICOLON'

def p_arithmeticExpressionNumber(p):
    'arithmeticExpression : value'
    #Aporte Luis Quezada p[0] = p[1]
    p[0] = p[1]

def p_arithmeticExpressionGroup(p):
    'arithmeticExpression : LPAREN arithmeticExpression RPAREN'
    #Aporte Luis Quezada p[0] = p[2]
    p[0] = p[2]

def p_arithmeticExpression(p):
    'arithmeticExpression : arithmeticExpression arithmeticOperator arithmeticExpression'
    #Aporte Luis Quezada Operacion entre numeros------------------------
    if not isinstance(p[len(p)-3], str) or p[len(p)-3] in variables:
        pass
    else:
        print(f'Error {p[len(p)-3]} no es un numero')
        return

    if not isinstance(p[len(p)-1], str) or p[len(p)-1] in variables:
        pass
    else:
        print(f'Error {p[len(p)-1]} no es un numero')
        return

    if not(p[len(p)-1] and p[len(p)-3]):
        return
    
    if p[len(p)-2] == "+":
        p[0] = p[len(p)-3] + p[len(p)-1]
    elif p[len(p)-2] == "-":
        p[0] = p[len(p)-3] - p[len(p)-1]
    elif p[len(p)-2] == "*":
        p[0] = p[len(p)-3] * p[len(p)-1]
    elif p[len(p)-2] == "/":
        p[0] = p[len(p)-3] / p[len(p)-1]
    elif p[len(p)-2] == "%":
        p[0] = p[len(p)-3] % p[len(p)-1]
    elif p[len(p)-2] == "**":
        p[0] = p[len(p)-3] ** p[len(p)-1]
    #Aporte Luis Quezada -----------------------------------------------

def p_value(p):
    '''value : ID
             | INTEGER
             | FLOAT
             | STRING
    '''
    #Aporte Luis Quezada
    if isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]

def p_arithmeticOperator(p):
    '''arithmeticOperator : PLUS
                          | MINUS 
                          | TIMES 
                          | DIVIDE
                          | MOD
                          | EXP
    '''
    #Aporte Luis Quezada p[0] = p[1]
    p[0] = p[1]

# LINE - LUIS QUEZADA
def p_line(p):
    '''line : variableAsignation SEMICOLON
            | stringConcatenation SEMICOLON
    '''
    
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

# COMPARING VALUES - LUIS QUEZADA 1>2 AND 2>1
def p_comparingValue(p):
    'comparingValue : value comparingSign value'

# LOGICAL
def p_logicalCondition(p):
    """logicalCondition : comparingValue
                        | comparingValue conditionOperator comparingValue
                        | LPAREN logicalCondition RPAREN
    
    """

def p_conditionOperator(p):
    """conditionOperator : AND
                         | OR
                         | XOR 
    """

# CONCAT KEVIN VALLE
def p_stringConcatenation(p):
    """stringConcatenation : value CONCAT value
                           | value CONCAT stringConcatenation
                           | stringConcatenation CONCAT value
    """


# Error rule for syntax errors
def p_error(p):
    error_message = "Error en -> {}".format(p)
    print(error_message)

'''
def p_error(p):
    global current_key
    error_message = "Error en -> {}".format(p)
    if current_key in resultados:
        resultados[current_key].append(error_message)
    else:
        resultados[current_key] = [error_message]

parser = yacc.yacc()

algoritmos = Generador_log.algoritmos_3
resultados = {}

for key, value in algoritmos.items():
    current_key = key 
    result = parser.parse(value)
    if current_key in resultados:
        resultados[current_key].append(str(result))
    else:
        resultados[current_key] = [str(result)]

        
Generador_log.generar_log_sintactico(resultados)
'''
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