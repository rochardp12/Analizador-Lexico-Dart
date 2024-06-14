#Grupo 7 - Analizador Léxico Dart

import ply.lex as lex

# List of token names.   This is always required
reserved = {"def":"DEF","return":"RETURN","print":"PRINT"}

tokens = (
   'INT',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
    'MOD',
    'VARIABLE',
    'COMA',
    'TWOPOINTS',
    'FLOAT'
)+tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MOD = r'%'
t_COMA = r','
t_TWOPOINTS = r':'


def t_VARIABLE(t):
    r'[_a-zA-Z]\w*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

# A regular expression rule with some action code
def t_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_FLOAT(t):
    r'((-)?(\d)+\.(\d)*|\.(\d)*)'
    t.value = float(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

data = """def function(a, b):
4*5=4+t
%6
.257
print(a)
PRINT(B)
return b"""

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)