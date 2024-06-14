import ply.lex as lex

# Todas las palabras reservadas Stefano Suarez
reserved = {"__halt_compiler()" : "HALT", "abstract" : "ABSTRACT", "and" : "AND", "array()" : "ARRAY", "as" : "AS", "break" : "BREAK",
"callable" : "CALLABLE", "case" : "CASE", "catch" : "CATCH", "class" : "CLASS", "clone" : "CLONE", "const" : "CONST", "continue" : "CONTINUE",
"declare" : "DECLARE", "default" : "DEFAULT", "die()" : "DIE", "do" : "DO", "echo" : "ECHO", "else" : "ELSE", "elseif" : "ELSEIF",
"empty()" : "EMPTY", "endwhile" : "ENDWHILE", "eval()" : "EVAL", "exit()" : "EXIT", "extends" : "EXTENDS", "final" : "FINAL", "finally" : "FINALLY",
"fn" : "FN", "for" : "FOR", "foreach" : "FOREACH", "function" : "FUNCTION", "global" : "GLOBAL", "goto" : "GOTO", "if" : "IF", "implements" : "IMPLEMENTS",
"include" : "INCLUDE", "include_once" : "INCLUDE_ONCE", "instanceof" : "INSTANCEOF", "insteadof" : "INSTEADOF", "interface" : "INTERFACE", "isset()" : "ISSET",
"list()" : "LIST", "match" : "MATCH", "namespace" : "NAMESPACE", "new" : "NEW", "or" : "OR", "print" : "PRINT", "private" : "PRIVATE", "protected" : "PROTECTED",
"public" : "PUBLIC", "require" : "REQUIRE", "require_once" : "REQUIRE_ONCE", "return" : "RETURN", "static" : "STATIC", "switch" : "SWITCH",
"throw" : "THROW", "trait" : "TRAIT", "try" : "TRY", "unset()" : "UNSET", "use" : "USE", "var" : "VAR", "while" : "WHILE", "xor" : "XOR",
"yield" : "YIELD", "yield_from" : "YIELD_FROM"}

# Lista de tokens
tokens= (
    'INT',
    'ID',
    'LPAREN',
    'RPAREN',
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
    'EQUAL',
    'IDENTICAL',
    'NOTEQUAL',
    'LESSTHAN',
    'GREATERTHAN',
    'LESSEQUALTHAN',
    'GREATEREQUALTHAN',
    'LOGICALAND',
    'LOGICALOR',
    'LOGICALNOT',
    'EXECUTION',
    'ERRORCONTROL',
    'CONCAT',
    'CONCATASSIGN',
    'OPEN_TAG',
    'DOC_COMMENT',
)+tuple(reserved.values())

# Lista Operadores - Kevin Valle
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
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
t_EQUAL = r'=='
t_IDENTICAL = r'==='
t_NOTEQUAL = r'!='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LESSEQUALTHAN = r'<='
t_GREATEREQUALTHAN = r'>='
    # Logico
t_LOGICALAND = r'and'
t_LOGICALOR = r'or'
t_LOGICALNOT = r'!'
    # Ejecucion
t_EXECUTION = r'^(`)([^`]*)(`)$'
    # Control Errores
t_ERRORCONTROL = r'@'
    # Cadenas
t_CONCAT = r'\.'
t_CONCATASSIGN = r'\.='
    # Tipo
#t_INSOF = r'instanceof'
# Lista Operadores - Kevin Valle

def t_OPEN_TAG(t):
    r'<(\?(php)?|%)'
    t.type = reserved.get(t.value, 'OPEN_TAG')
    return t
#Comentario
def t_DOC_COMMENT(t):
    r'\/\*(.|\n)*?\*\/'
    t.type = reserved.get(t.value, 'DOC_COMMENT')
    return t

# Expresiones regulares para tokens simples
def t_ID(t):
    r'[a-zA-Z_$]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Regla de manejo de errores
def t_error(t):
    print("Illegal character '%s" % t.value[0])
    t.lexer.skip(1)

# Constructor lexer
lexer = lex.lex()

data = "$hola abstract"

# ALGORITMO PARA PRUEBA DE OPERADORES - GENERADO POR IA - Kevin Valle
dataOperadores = '''
    <?php
    $var = 5;
    $var++;
    $arr[0] = $var;
    echo $arr[0];
    if ($var == $arr[0]) {
        echo "Equal";
    }
    $command = `ls`;
    ?>
    '''

lexer.input(dataOperadores)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
            break   # No more input
    print(tok)