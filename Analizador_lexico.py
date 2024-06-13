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
    'ID'
)+tuple(reserved.values())

#Expresiones regulares para tokens simples
def t_ID(t):
    r'[a-zA-Z_$]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s" % t.value[0])
    t.lexer.skip(1)

# Constructor lexer
lexer = lex.lex()

data = "__halt_compiler() abstract"

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
            break   # No more input
    print(tok)