#Grupo 7 - Analizador Léxico Dart

import ply.lex as lex
import os
from datetime import datetime

# List of token names.   This is always required
reserved = {
    "def":"DEF",
    "return":"RETURN",
    "print": "PRINT",
    #Katherine Tumbaco
    "enum": "ENUM",
    "void": "VOID",
    "main": "MAIN",
    "for": "FOR",
    "var": "VAR",
    "in": "IN",
    "break": "BREAK",
    "List": "LIST",
    }

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
    'FLOAT',
    #Katherine Tumbaco
   'LLlave',
   'RLlave',
   'LCORC',
   'RCORC',
   'SEMICOLON',
   'EQUALS',
   'POINT',
   'Lmenor',
   'Rmayor'
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
#Katherine Tumbaco
t_LLlave  = r'\{'
t_RLlave  = r'\}'
t_Lmenor   = r'\<'
t_Rmayor   = r'\>'
t_LCORC = r'\['
t_RCORC = r'\]'
t_SEMICOLON = r';'
t_EQUALS   = r'='
t_POINT      = r'\.'


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
    r'(\d+\.\d+|\.\d+)'
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

#Generate logs
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

usuarioGit = "katumbac"
current_time = datetime.now().strftime("%d%m%Y-%Hh%M")
log_filename = f"lexico-{usuarioGit}-{current_time}.txt"
log_filepath = os.path.join(log_dir, log_filename)

data = """def function(a, b):
4*5=4+t
%6
.257
print(a)
PRINT(B)
return b"""

#Katherine Tumbaco
algoritmoKatherine = '''
enum DiaSemana{
    Lunes,
    Martes,
    Miercoles,
    Jueves,
    Viernes,
    Sabado,
    Domingo
}

void main(){
    
    List<DiaSemana> diaSemana = [
        DiaSemana.Lunes, DiaSemana.Martes, DiaSemana.Miercoles, DiaSemana.Jueves, 
        DiaSemana.Viernes, DiaSemana.Sabado, DiaSemana.Domingo
    ];
    
    for ( var dia in diaSemana){
        print(dia);
        if (dia == DiaSemana.Sabado){
            break;
        }
        
    }
} 

'''

lexer.input(algoritmoKatherine)

# Tokenize
with open(log_filepath, 'w') as log_file:
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        log_file.write(f"{tok}\n")
        print(tok)