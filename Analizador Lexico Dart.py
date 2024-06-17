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
    'NEWDATATYPE',
    'INTERNDATATYPE',
    'COMMA',
    'NUMBERINT',
    'BOOLTEXT',
    'DATAATTRIBUTE',
    'COLON',
    'DATAFUNCTION',
    'ASSIGN',
    'FUNCTION'
    )+tuple(reserved.values())

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
t_ASSIGN = r'='
asdas

#Richard Perez

def t_NEWDATATYPE(t):
    r'[A-Z][_a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'NEWDATATYPE')
    return t

def t_FUNCTION(t):
    r'[a-zA-Z]+\w*\(\w*\)'
    t.type = reserved.get(t.value, 'FUNCTION')
    return t

def t_DATAFUNCTION(t):
    r'\.[a-zA-Z]+\w*\(\w*\)'
    t.type = reserved.get(t.value, 'DATAFUNCTION')
    return t

def t_BOOLTEXT(t):
    r'true|false'
    if t.value == 'true':
        t.value = True
    else:
        t.value = False    
    return t

def t_VARIABLE(t):
    r'[_a-zA-Z]\w*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_COMMENT(t):
    r'//.*'
    t.type = reserved.get(t.value, 'COMMENT')
    return t

def t_STRINGTEXT(t):
    r'"[^"]*"'
    t.type = reserved.get(t.value, 'STRINGTEXT')
    return t

def t_INTERNDATATYPE(t):
    r'\<[A-Z][_a-zA-Z0-9]*\>'
    t.type = reserved.get(t.value, 'INTERNDATATYPE')
    return t

def t_DATAATTRIBUTE(t):
    r'\.[a-zA-Z_]+\w*'
    t.type = reserved.get(t.value, 'DATAATTRIBUTE')
    return t


# A regular expression rule with some action code
def t_NUMBERINT(t):
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

data = """
        class Pais {
        String nombre;
        bool ganoMundial;
        int cantidad;

        Pais(this.nombre, this.ganoMundial, this.cantidad);

        public String cantidadMundiales() => print(this.cantidad)
        }

        void main() {
        // Crear un conjunto de países
        Set<Pais> paises = {
            Pais("Brasil", true, 5),
            Pais("Argentina", true, 3),
            Pais("España", true, 1),
            Pais("Italia", true, 4),
            Pais("México", false, 0),
            Pais("Japón", false, 0),
        };
        // Recorrer el conjunto de países y aplicar el switch en ganoMundial
        for (Pais pais in paises) {
            switch (pais.ganoMundial) {
            case true:
                print("GANÓ:  ${pais.nombre}");
                pais.cantidadMundiales();
                break;
            case false:
                print("NO GANÓ:  ${pais.nombre}");
                break;
            case default:
                print("Sin Informacion");
            }
        }
        }
        """

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)