#Nombre: Roberto Encalada
#Matricula: 202101507
import ply.lex as lex

# List of token names.   This is always required
reserved = {
    'main': 'MAIN',
    'new': 'NEW',
    'this': 'THIS',
    'null': 'NULL',
    'list': 'LIST',
    'map': 'MAP',
    'class': 'CLASS',
    'public': 'PUBLIC',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'static': 'STATIC',
    'abstract': 'ABSTRACT',
    'interface': 'INTERFACE',
    'extends': 'EXTENDS',
    'module': 'MODULE',
    'def': 'DEF',
    'method': "METHOD", 
    'void': 'VOID', 
    'var': 'VAR', 
    'string':'STRING', 
    'int':'INT',
    'final':'FINAL',
    'dynamic':'DYNAMIC',
    'double':'DOUBLE',
    'const':'CONST',
    'boolean':'BOOLEAN',
    'typedef':'TYPEDEF',
    'print':'PRINT',
    'for':'FOR',
    'while':'WHILE',
    'if':'IF',
    'else':'ELSE',
    'return':'RETURN',
    'break':'BREAK',
    'switch':'SWITCH',
    'case':'CASE',
    'try':'TRY',
    'catch':'CATCH',
    'finally':'FINALLY',
    'True':'TRUE',
    'False':'FALSE',
    'as':'AS',
    'is':'IS',
    'enum':'ENUM',
    'super':'SUPER',
    }
tokens = (
    'NUMBER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'LANGLE',
    'RANGLE',
    'MOD',
    'INTEGERDIVISION',
    'VARIABLE',
    'CLASS',
    'COMMA',
    'EQUALS',
    'NEQ',
    'TWODOTS',
    'DOTCOMMA',
    'APHOSTROPHE',
    'DOUBLEAPHOSTROPHE',
    'ADMIRATION',
    'DOLLAR',
    'OR',
    'AND',
    'commentLine',
    'commentBlock',


) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MOD     = r'%'
t_INTEGERDIVISION = r'~/'
t_COMMA   = r','
t_EQUALS  = r'='
t_NEQ = r'!='
t_TWODOTS = r':'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOTCOMMA = r';'
t_LANGLE = r'<'
t_RANGLE = r'>'
t_APHOSTROPHE = r'\''
t_DOUBLEAPHOSTROPHE = r'\"'
t_ADMIRATION = r'!'
t_DOLLAR = r'\$'
t_OR = r'\|\|'
t_AND = r'&&'
t_commentLine = r'//.*'
t_commentBlock = r'/\*(.|\n)*?\*/'

def t_VARIABLE(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value,'VARIABLE')    # Check for reserved words
    return t
# A regular expression rule with some action code

def t_FLOAT(t):
    r'\d*\.{1}\d*'
    t.value = float(t.value)
    return t
    
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
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

data = """void main() {
  // Error léxico: variable con nombre inválido
  var 123variable = 10;

  // Error sintáctico: falta de cierre de paréntesis
  for (var i = 0; i < 10; i++) {
    print('Número: $i');
  
  // Error semántico: operación inválida entre un entero y una cadena
  var x = 10;
  var y = 'Hola, mundo!';
  print(x + y);
  /* comentario */
}
"""

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)