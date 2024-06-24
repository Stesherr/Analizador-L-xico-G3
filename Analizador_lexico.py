import ply.lex as lex
import Generador_log

# Todas las palabras reservadas Stefano Suarez
reserved = {"__halt_compiler()" : "__HALT_COMPILER", "abstract" : "ABSTRACT", "and" : "AND", "array()" : "ARRAY", "as" : "AS", 
"break" : "BREAK", "callable" : "CALLABLE", "case" : "CASE", "catch" : "CATCH", "class" : "CLASS", "clone" : "CLONE", "const" : "CONST", "continue" : "CONTINUE",
"declare" : "DECLARE", "default" : "DEFAULT", "die()" : "DIE", "do" : "DO", "echo" : "ECHO", "else" : "ELSE", "elseif" : "ELSEIF",
"empty()" : "EMPTY", "endwhile" : "ENDWHILE", "eval()" : "EVAL", "exit()" : "EXIT", "extends" : "EXTENDS", "final" : "FINAL", "finally" : "FINALLY",
"fn" : "FN", "for" : "FOR", "foreach" : "FOREACH", "fgets" : "FGETS", "function" : "FUNCTION", "global" : "GLOBAL", "goto" : "GOTO", "if" : "IF", "implements" : "IMPLEMENTS",
"include" : "INCLUDE", "include_once" : "INCLUDE_ONCE", "instanceof" : "INSTANCEOF", "insteadof" : "INSTEADOF", "interface" : "INTERFACE", "isset()" : "ISSET",
"list()" : "LIST", "match" : "MATCH", "namespace" : "NAMESPACE", "new" : "NEW", "or" : "OR", "print" : "PRINT", "private" : "PRIVATE", "protected" : "PROTECTED", "push" : "PUSH", "pop()" : "POP",
"public" : "PUBLIC", "require" : "REQUIRE", "require_once" : "REQUIRE_ONCE", "return" : "RETURN", "static" : "STATIC", "switch" : "SWITCH",
"throw" : "THROW", "trait" : "TRAIT", "try" : "TRY", "unset()" : "UNSET", "use" : "USE", "var" : "VAR", "while" : "WHILE", "xor" : "XOR",
"yield" : "YIELD", "yield_from" : "YIELD_FROM", "SplQueue()" : "QUEUE", "SplStack()" : "STACK", "STDIN" : "STDIN"}

# Lista de tokens
tokens= (
    'SEMICOLON',
    'INTEGER',
    'FLOAT',
    'STRING',
    'BOOL',
    'NULL',
    'ID',
    'LPAREN',
    'RPAREN',
    'LSQUARE',
    'RSQUARE',
    'LCURLY',
    'RCURLY',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'EXP',
    'EQUAL',
    'PLUSASSIGN',
    'MINUSASSIGN',
    'TIMESASSIGN',
    'DIVIDEASSIGN',
    'MODASSIGN',
    'EXPASSIGN',
    'INCREMENT',
    'DECREMENT',
    'BITAND',
    'BITOR',
    'BITNOT',
    'IS_EQUAL',
    'IDENTICAL',
    'NOTEQUAL',
    'LESSTHAN',
    'GREATERTHAN',
    'LESSEQUALTHAN',
    'GREATEREQUALTHAN',
    'LOGICALNOT',
    'EXECUTION',
    'ERRORCONTROL',
    'CONCAT',
    'CONCATASSIGN',
    'OBJOP',
    'OPEN_TAG',
    'CLOSE_TAG',
    'DOC_COMMENT',
    'COLON',
    'FNARROW',
    'QUOTE',
    'COMMA',
    'DOUBLEQUOTE'
)+tuple(reserved.values())

# Lista Operadores - Kevin Valle
t_SEMICOLON = r';'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_COLON = r':'
t_QUOTE = r'\''
t_DOUBLEQUOTE = r'\"'
t_COMMA = r','
    # Aritmeticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_MOD = r'%'
t_EXP = r'\*\*'
    # Asignacion (Aritmetica)
t_EQUAL = r'='
t_PLUSASSIGN = r'\+='
t_MINUSASSIGN = r'-='
t_TIMESASSIGN = r'\*='
t_DIVIDEASSIGN = r'\/='
t_MODASSIGN = r'%='
t_EXPASSIGN = r'\*\*='
    # Incremento/Decremento
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
    # Bit a Bit
t_BITAND = r'\$'
t_BITOR = r'\|'
t_BITNOT = r'~'
    # Comparacion
t_IS_EQUAL = r'=='
t_IDENTICAL = r'==='
t_NOTEQUAL = r'!='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LESSEQUALTHAN = r'<='
t_GREATEREQUALTHAN = r'>='
    # Logico
t_LOGICALNOT = r'!'
    # Control Errores
t_ERRORCONTROL = r'@'
    # Cadenas
t_CONCAT = r'\.'
t_CONCATASSIGN = r'\.='
    # Objeto
t_OBJOP = r'->'
    # Funciones
t_FNARROW = r'=>'
# Lista Operadores - Kevin Valle

#OPEN/CLOSE TAG Luis Quezada
def t_OPEN_TAG(t):
    r'<(\?(php)?|%)'
    t.type = reserved.get(t.value, 'OPEN_TAG')
    return t
def t_CLOSE_TAG(t):
    r'(\?|%)>'
    t.type = reserved.get(t.value, 'CLOSE_TAG')
    return t
#Comentario Luis Quezada
def t_DOC_COMMENT(t):
    r'(\/\*(.|\n)*?\*\/)|(\/\/.*)'
    t.type = reserved.get(t.value, 'DOC_COMMENT')
    return t

# Palabras reservadas compuestas - Stefano Suarez
def t_HALT_COMPILER(t):
     r'__halt_compiler\(\)'
     t.type = reserved.get(t.value, '__HALT_COMPILER')
     return t

def t_ARRAY(t):
     r'array\(\)'
     t.type = reserved.get(t.value, 'ARRAY')
     return t

def t_QUEUE(t):
    r'SplQueue\(\)'
    t.type = reserved.get(t.value, 'QUEUE')
    return t

def t_POP(t):
    r'pop\(\)'
    t.type = reserved.get(t.value, 'POP')
    return t

def t_STACK(t):
    r'SplStack\(\)'
    t.type = reserved.get(t.value, 'STACK')
    return t

def t_DIE(t):
     r'die\(\)'
     t.type = reserved.get(t.value, 'DIE')
     return t

def t_EMPTY(t):
     r'empty\(\)'
     t.type = reserved.get(t.value, 'EMPTY')
     return t

def t_EVAL(t):
     r'eval\(\)'
     t.type = reserved.get(t.value, 'EVAL')
     return t

def t_EXIT(t):
     r'exit\(\)'
     t.type = reserved.get(t.value, 'EXIT')
     return t

def t_ISSET(t):
     r'isset\(\)'
     t.type = reserved.get(t.value, 'ISSET')
     return t

def t_LIST(t):
     r'list\(\)'
     t.type = reserved.get(t.value, 'LIST')
     return t

def t_UNSET(t):
     r'unset\(\)'
     t.type = reserved.get(t.value, 'UNSET')
     return t

# Variables - Stefano Suarez
def t_ID(t):
    r'[a-zA-Z_$][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_EXECUTION(t):
     r'`([^`]*)`'
     t.type = reserved.get(t.value, 'EXECUTION')
     return t

# Tipos de Datos - Kevin Valle
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
     r'([-]?)(\d+\.\d*|\.\d+)'
     t.value = float(t.value)
     return t

def t_STRING(t):
     r'(")([^"]+)(")'
     t.value = str(t.value)
     return t
# Tipos de Datos - Kevin Valle

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Regla para manejar nuevas líneas - Stefano Suarez
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

# Regla de manejo de errores - Stefano Suarez
def t_error(t):
    #print("Illegal character '%s" % t.value[0])
    t.lexer.skip(1)

# Constructor lexer
lexer = lex.lex()

# ALGORITMO PARA PRUEBA DE OPERADORES
Generador_log.obtener_alg()
# RESULTADOS
algoritmos = Generador_log.algoritmos_3
resultados = {}

for key, value in algoritmos.items():
    lexer.input(value)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
                break
        if key in resultados:
             resultados[key].append(str(tok))
        else:
             resultados[key]  = [str(tok)]

#Generador_log.generar_log(resultados)