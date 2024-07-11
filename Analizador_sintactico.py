import ply.yacc as yacc
from Analizador_lexico import tokens
import Generador_log
import math

syntax_error = []
semantic_error = []

variables = {}
mathFunctions = {"abs", "sin", "cos", "tan", "pi"}
#Aporte Stefano Suarez
precedence = (
    ('left', 'AND', 'OR', 'XOR'),
    ('left', 'LESSTHAN', 'GREATERTHAN', 'LESSEQUALTHAN', 'GREATEREQUALTHAN', 'IS_EQUAL', 'NOTEQUAL'),
    ('right', 'EQUAL')
)

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
              | stringConcatenation
              | callFunction
    '''
    #Aporte Stefano Suarez
    p[0] = p[1]

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
    '''if_elseStatement : IF LPAREN logicalCondition RPAREN LCURLY ifStatementBody RCURLY ELSE LCURLY ifStatementBody RCURLY
                        | IF LPAREN logicalCondition RPAREN LCURLY ifStatementBody
                        '''
    #Aporte Stefano Suarez - Revisa que la condicion del if sea un tipo booleano
    if len(p) == 12:
        p[0] = ('if_else', p[3], p[6], p[10])
    else:
        p[0] = ('if', p[3], p[6])

    if not isinstance(p[3], bool):
        error_message = (f"Error la condicion del 'if' debe ser un booleano, no '{type(p[3]).__name__}'")
        semantic_error.append(error_message)
def p_ifStatementBody(p):
    '''ifStatementBody : cuerpo
                       | cuerpo CONTINUE SEMICOLON
                       | ifStatementBody cuerpo
                       '''
    #Aporte Stefano Suarez
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = (p[1], 'continue')
    else:
        p[0] = p[1] + p[2]

# ESTRUCTURA FOR - LUIS QUEZADA
def p_forStatement(p):
    'forStatement : FOR LPAREN forStatementCondition RPAREN LCURLY forStatementBody RCURLY'
    #Aporte Stefano Suarez
    p[0] = ('for', p[3], p[6])

def p_forStatementCondition(p):
    '''forStatementCondition :  SEMICOLON SEMICOLON 
                            |  variableAsignation SEMICOLON SEMICOLON variableAsignation
                            |  variableAsignation SEMICOLON comparingValue SEMICOLON variableAsignation
                            '''
    #Aporte Stefano Suarez - Revisa que la condicion del for sea un tipo booleano
    if len(p) == 3:
        p[0] = ('for_cond', None, None, None)
    elif len(p) == 5:
        p[0] = ('for_cond', p[1], None, p[4])
    elif len(p) == 6:
        if not isinstance(p[3], bool):
            error_message = (f"Error la condicion del 'for' deber ser un booleano, no '{type(p[3]).__name__}'")
            semantic_error.append(error_message)
            print(error_message)
        p[0] = ('for_cond', p[1], p[3], p[5])

def p_forStatementBody(p):
    '''forStatementBody : cuerpo 
                        | forStatementBody cuerpo
                        '''
    #Aporte Stefano Suarez
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

#ESTRUCTURA ARREGLO - LUIS QUEZADA
def p_arrayAsignation(p):
    'arrayAsignation : VAR EQUAL arrayDeclaration SEMICOLON'

def p_arrayDeclaration(p):
    ''' arrayDeclaration : ARRAY arraysValues RPAREN
                        | LSQUARE arraysValues RSQUARE
                        | arrayValue 
                        '''

def p_arraysValues(p):
    ''' arraysValues : arrayValue 
                    | arraysValues COMMA arrayValue
                    '''

def p_arrayValue(p):
    '''arrayValue : ARRAY values RPAREN
                    | LSQUARE values RSQUARE
                    '''

# ESTRUCTURA COLA - STEFANO SUAREZ
def p_stackDeclaration(p):
    'stackDeclaration : VAR EQUAL NEW STACK SEMICOLON'

def p_stackPush(p):
    'stackPush : VAR OBJOP PUSH LPAREN value RPAREN SEMICOLON'

def p_stackPop(p):
    'stackPop : VAR OBJOP POP SEMICOLON'

# ESTRUCTURA COLA - KEVIN VALLE
def p_queueDeclaration(p):
    'queueDeclaration : VAR EQUAL NEW QUEUE SEMICOLON'

def p_queueEnqueue(p):
    'queueEnqueue : VAR OBJOP PUSH LPAREN value RPAREN SEMICOLON'

def p_queueDequeue(p):
    'queueDequeue : VAR OBJOP POP SEMICOLON'

# DEFINE FUNCTION - LUIS QUEZADA
def p_defineFunction(p):
    '''defineFunction : FUNCTION ID LPAREN arguments RPAREN LCURLY programa RCURLY
                    | FUNCTION ID LPAREN RPAREN LCURLY programa RCURLY
                    '''

# ARGUMENTS - LUIS QUEZADA
def p_arguments(p):
    '''arguments : VAR
                | VAR COMMA arguments
                '''
    
# FUNCION ANONIMA - STEFANO SUAREZ
def p_anonymousFunction(p):
    '''anonymousFunction : FUNCTION LPAREN RPAREN LCURLY cuerpo RCURLY 
                         | FUNCTION LPAREN arguments RPAREN LCURLY cuerpo RCURLY
                         '''

#  FUNCION FLECHA - KEVIN VALLE
def p_arrowFunction(p):
    'arrowFunction : FN LPAREN VAR RPAREN FNARROW arrowBody SEMICOLON'

def p_arrowBody(p):
    '''arrowBody : FN LPAREN VAR RPAREN FNARROW arrowBody
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
    'fgets : VAR EQUAL FGETS LPAREN STDIN RPAREN SEMICOLON'

def p_arithmeticExpressionNumber(p):
    'arithmeticExpression : value'
    #Aporte Luis Quezada p[0] = p[1]
    p[0] = p[1]

#Aporte Kevin Valle - Conversion Implicita -----
def p_arithmeticExpressionCastInt(p):
    'arithmeticExpression : STRING'
    if p[1].isdigit():
        p[0] = int(p[1].strip('"'))

#Aporte Kevin Valle - Conversion Implicita -----

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
        error_message = f'Error {p[len(p)-3]} no es un numero'
        semantic_error.append(error_message)
        
    if not isinstance(p[len(p)-1], str) or p[len(p)-1] in variables:
        pass
    else:
        error_message = f'Error {p[len(p)-1]} no es un numero'
        semantic_error.append(error_message)

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

#callFuntion Luis Quezada------------------------------------------------------
def p_callFunction(p):
    'callFunction : ID LPAREN RPAREN SEMICOLON'
    if p[1] in mathFunctions:
        if p[1] == "pi":
            p[0] = math.pi
        elif p[1] == "abs" or p[1] == "sin" or p[1] == "cos" or p[1] == "tan":
            error_message = 'Error, faltan argumentos'
            semantic_error.append(error_message)
        

def p_callFunctionArguments(p):
    'callFunction : ID LPAREN value RPAREN SEMICOLON'
    if p[1] in mathFunctions:
        if not isinstance(p[3], str) or p[3] in variables:
            pass
        else:
            error_message = f'Error, {p[3]} no es un argumento valido'
            semantic_error.append(error_message)
        if p[1] == "abs":
            p[0] = abs(p[3])
        elif p[1] == "sin":
            p[0] = math.sin(p[3])
        elif p[1] == "cos":
            p[0] = math.cos(p[3])
        elif p[1] == "tan":
            p[0] = math.tan(p[3])
        elif p[1] == "pi":
            error_message = f'Error, {p[1]} no requiere de argumentos'
            semantic_error.append(error_message)
#callFuntion Luis Quezada------------------------------------------------------

def p_value(p):
    '''value : VAR
             | INTEGER
             | FLOAT
             | STRING
             | stringConcatenation
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
    '''
    p[0] = p[1]
    
# VARIABLE ASIGNATION - LUIS QUEZADA
def p_variableAsignation(p):
    '''variableAsignation : VAR EQUAL value
                          | VAR EQUAL arithmeticExpression
                          | VAR INCREMENT
                          | VAR DECREMENT
                          | VAR EQUAL stringConcatenation
                          | VAR EQUAL anonymousFunction
    '''
    #Aporte Stefano Suarez y Luis Quezada
    if len(p) == 4:
        variables[p[1]] = p[3]
    else:
        if not p[1] in variables:
            error_message = f'Error, {p[1]} no ha sido inicializado.'
            semantic_error.append(error_message)
            return
        if (isinstance(variables[p[1]], int) or isinstance(variables[p[1]], float)):
            if p[2] == "++":
                variables[p[1]] = variables[p[1]] + 1
            elif p[2] == "--":
                variables[p[1]] = variables[p[1]] - 1
        else:
            error_message = f'Error, {p[1]} no es una variable a la que se le pueda aplicar estas operaciones.'
            semantic_error.append(error_message)

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
    #Aporte Stefano Suarez
    p[0] = p[1]

# COMPARING VALUES - LUIS QUEZADA 1>2 AND 2>1
def p_comparingValue(p):
    'comparingValue : value comparingSign value'
    #Aporte Stefano Suarez - Validar que los valores sean del mismo tipo
    if type(p[1]) != type(p[3]):
        error_message = (f"Error: los operandos deben ser del mismo tipo, pero se encontró {type(p[1]).__name__} y {type(p[3]).__name__}")
        semantic_error.append(error_message)
    else:
        if p[2] == '<':
            p[0] = p[1] < p[3]
        elif p[2] == '>':
            p[0] = p[1] > p[3]
        elif p[2] == '==':
            p[0] = p[1] == p[3]
        elif p[2] == '!=':
            p[0] = p[1] != p[3]
        elif p[2] == '<=':
            p[0] = p[1] <= p[3]
        elif p[2] == '>=':
            p[0] = p[1] >= p[3]
        elif p[2] == '===':
            p[0] = p[1] is p[3]

# LOGICAL
def p_logicalCondition(p):
    """logicalCondition : comparingValue
                        | comparingValue conditionOperator comparingValue
                        | LPAREN logicalCondition RPAREN
    """
    #Aporte Stefano Suarez - Identificar el tipo de operador de condicion
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4 and p[1] == '(':
        p[0] = p[2]
    elif len(p) == 4:
        if p[2] == '&&':
            p[0] = p[1] and p[3]
        elif p[2] == '||':
            p[0] = p[1] or p[3]
        elif p[2] == 'xor':
            p[0] = bool(p[1]) != bool(p[3])

def p_conditionOperator(p):
    """conditionOperator : AND
                         | OR
                         | XOR 
    """
    #Aporte Stefano Suarez
    p[0] = p[1]
    

# Aporte Kevin Valle --- Conversion Concatenacion Int con String
def p_stringConcatenationGroup(p):
    'stringConcatenation : value CONCAT value'
    try:
        p[0] = str(p[1]) + str(p[3])
    except ValueError:
        return

def p_stringConcatenation(p):
    'stringConcatenation : stringConcatenation CONCAT stringConcatenation'
    if isinstance(p[len(p)-3], str) or p[len(p)-3] in variables:
        pass
    else:
        error_message = f'Error al concatenar {p[len(p)-3]}'
        semantic_error.append(error_message)
        
    if isinstance(p[len(p)-1], str) or p[len(p)-1] in variables:
        pass
    else:
        error_message = f'Error al concatenar {p[len(p)-1]}'
        semantic_error.append(error_message)

    if not(p[len(p)-1] and p[len(p)-3]):
        return
    
    #p[0] = p[len(p)-3] + p[len(p)-1]
# Aporte Kevin Valle --- Conversion Concatenacion Int con String

def p_error(p):
    error_message = f"Error en ->: {p}"
    syntax_error.append(error_message)
    
parser = yacc.yacc()