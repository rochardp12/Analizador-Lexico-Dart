#Grupo 7 - Analizador Léxico Dart

import ply.lex as lex

# List of token names.   This is always required
reserved = {
    #Richard Perez
    "class": "CLASS",
    "String": "STRING",
    "bool": "BOOL",
    "int": "INT",
    "this": "THIS",
    "public": "PUBLIC",
    "print": "PRINT",
    "void": "VOID",
    "main": "MAIN",
    "Set": "SET",
    "for": "FOR",
    "in": "IN",
    "switch": "SWITCH",
    "case": "CASE",
    "break": "BREAK",
    "default": "DEFAULT"
    }

tokens = (
    #Richard Perez
    'VARIABLE',
    'LCURLYBRACE',
    'RCURLYBRACE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'ARROWFUNCTION',
    'DOT',
    'COMMENT',
    'STRINGTEXT',
    'NEWDATATYPE'
    'INTERNDATATYPE',
    'COMMA',
    'NUMBER',
    'BOOLTEXT',
    'ATTRIBUTE',
    'COLON',
    'ADDEDSTRING',
    'FUNCTION'
    )+tuple(reserved.values())



'''
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
)+tuple(reserved.values())'''

# Regular expression rules for simple tokens

#Richard Perez
t_LCURLYBRACE = r'\{'
t_RCURLYBRACE = r'\}'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMICOLON = r';'
t_ARROWFUNCTION = r'=>'
t_DOT = r'\.'
t_COMMA = r','
t_COLON = r':'


'''
    'VARIABLE',
    'COMMENT',
    'STRINGTEXT',
    'NEWDATATYPE'
    'INTERNDATATYPE',
    'NUMBER',
    'BOOLTEXT',
    'ATTRIBUTE',
    'ADDEDSTRING',
    'FUNCTION'''



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