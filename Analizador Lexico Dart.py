import ply.lex as lex
import os
from datetime import datetime

# List of token names.   This is always required
reserved = {
    #Roberto Encalada
    'main': 'MAIN',
    'new': 'NEW',
    'null': 'NULL',
    'map': 'MAP',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'static': 'STATIC',
    'abstract': 'ABSTRACT',
    'interface': 'INTERFACE',
    'extends': 'EXTENDS',
    'module': 'MODULE',
    'def': 'DEF',
    'method': "METHOD", 
    'final':'FINAL',
    'dynamic':'DYNAMIC',
    'double':'DOUBLE',
    'const':'CONST',
    'typedef':'TYPEDEF',
    'while':'WHILE',
    'if':'IF',
    'else':'ELSE',
    'elif':'ELIF',
    'return':'RETURN',
    'try':'TRY',
    'catch':'CATCH',
    'finally':'FINALLY',
    'True':'TRUE',
    'False':'FALSE',
    'as':'AS',
    'is':'IS',
    'super':'SUPER',
    #Richard Perez
    "class": "CLASS",
    "String": "STRING",
    "int": "INT",
    "this": "THIS",
    "public": "PUBLIC",
    "print": "PRINT",
    "Set": "SET",
    "switch": "SWITCH",
    "case": "CASE",
    "default": "DEFAULT",
    #Katherine Tumbaco
    "enum": "ENUM",
    "void": "VOID",
    "for": "FOR",
    "var": "VAR",
    "in": "IN",
    "break": "BREAK",
    "List": "LIST"
    }
tokens = (
    #Katherine Tumbaco
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
    #Roberto Encalada
    'MOD',
    'INTEGERDIVISION',
    'VARIABLE',
    'COMMA',
    'EQUALS',
    'NEQ',
    'DOT',
    'TWODOTS',
    'DOTCOMMA',
    'ADMIRATION',
    'DOLLAR',
    'OR',
    'AND',
    'commentLine',
    'commentBlock',
    'CHAINCHAR',
    #Richard Perez
    'ARROWFUNCTION',
    'NEWDATATYPE',
    'INTERNDATATYPE',
    'NUMBERINT',
    'DATAATTRIBUTE',
    'DATAFUNCTION',
    'FUNCTION'
) + tuple(reserved.values())

# Regular expression rules for simple tokens

#Katherine Tumbaco
t_NEQ = r'!='
t_DOT = r'\.'
t_TWODOTS = r':'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOTCOMMA = r';'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MINUS = r'-'
#Roberto Encalada
t_LANGLE = r'<'
t_RANGLE = r'>'
t_ADMIRATION = r'!'
t_DOLLAR = r'\$'
t_OR = r'\|\|'
t_AND = r'&&'
t_commentLine = r'//.*'
t_commentBlock = r'/\*(.|\n)*?\*/'
t_CHAINCHAR = r'(\'[^\']*\'|\"[^\"]*\")'
#Richard Perez
t_MOD     = r'\%'
t_INTEGERDIVISION = r'~/'
t_COMMA   = r','
t_EQUALS  = r'='
t_ARROWFUNCTION = r'=>'
t_PLUS    = r'\+'

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

#Roberto Encalada
def t_INTERNDATATYPE(t):
    r'\<[A-Z][_a-zA-Z0-9]*\>'
    t.type = reserved.get(t.value, 'INTERNDATATYPE')
    return t

def t_DATAATTRIBUTE(t):
    r'\.[a-zA-Z_]+\w*'
    t.type = reserved.get(t.value, 'DATAATTRIBUTE')
    return t

#Katherine Tumbaco
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
    
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value,'VARIABLE')    # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)




#Katherine Tumbaco
algoritmoKatherine = """
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

"""

algoritmoRichard = """
        class Pais {
        String nombre;
        boolean ganoMundial;
        int cantidad;

        Pais(this.nombre, this.ganoMundial, this.cantidad);

        public String cantidadMundiales() => print(this.cantidad)
        }

        void main() {
        // Crear un conjunto de países
        Set<Pais> paises = {
            Pais("Brasil", True, 5),
            Pais("Argentina", True, 3),
            Pais("España", True, 1),
            Pais("Italia", True, 4),
            Pais("México", False, 0),
            Pais("Japón", False, 0),
        };
        // Recorrer el conjunto de países y aplicar el switch en ganoMundial
        for (Pais pais in paises) {
            switch (pais.ganoMundial) {
            case True:
                print("GANÓ:  ${pais.nombre}");
                pais.cantidadMundiales();
                break;
            case False:
                print("NO GANÓ:  ${pais.nombre}");
                break;
            case default:
                print("Sin Informacion");
            }
        }
        }
        """
AlgoritmoRoberto = """
/* Block comment example
This is a test for the block comment token.
*/

// Line comment example
public class TestClass {
    private int number = 42;
    public double decimalNumber = 3.14;
    protected isValid = True;
    static final String CONSTANT_STRING = "Hello";
    private List<Integer> myList = new ArrayList<>();
    private Map<String, Integer> myMap = new HashMap<>();

    public static void main(String[] args) {
        TestClass instance = new TestClass();
        instance.testMethod();
    }

    public void testMethod() {
        int localVar = 10;
        double pi = 3.14;
        eanean flag = False;
        String greeting = "Hello, World!";
        char initial = 'A';
        
        if (localVar > 5 && flag == False) {
            print("localVar is greater than 5");
        } else {
            print("localVar is less than or equal to 5");
        }

        for (int i = 0; i < 10; i++) {
            myList.add(i);
        }

        while (localVar > 0) {
            localVar--;
        }

        switch (localVar) {
            case 0:
                print("localVar is zero");
                break;
            default:
                print("localVar is not zero");
                break;
        }

        try {
            int result = localVar / 0;
        } catch (ArithmeticException e) {
            print("Division by zero!");
        } finally {
            print("End of try-catch block");
        }

        number = (int) pi; // Casting
        myMap.put("Key", 123);

        // Check reserved words
        nullCheck(null);
        thisCheck(this);
        superCheck(super.toString());

        print(greeting + " " + initial + '!');
    }

    private void nullCheck(Object obj) {
        if (obj == null) {
            print("Object is null");
        }
    }

    private void thisCheck(TestClass obj) {
        if (obj == this) {
            print("This object");
        }
    }

    private void superCheck(String str) {
        if (str != null) {
            print("Super check passed");
        }
    }

    private void print(String message) {
        System.out.println(message);
    }
}
"""
algoritmos = [algoritmoKatherine, algoritmoRichard, AlgoritmoRoberto]
# Build the lexer
lexer = lex.lex()

#Generate logs
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

UsuariosGit = ["katumbac", "rochardp12", "rocaenca"]
current_time = datetime.now().strftime("%d%m%Y-%Hh%M")


for i in range(len(algoritmos)):
  log_filename = f"lexico-{UsuariosGit[i]}-{current_time}.txt"
  log_filepath = os.path.join(log_dir, log_filename)
  lexer.input(algoritmos[i])
  # Tokenize
  with open(log_filepath, 'w') as log_file:
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
        log_file.write(f"{tok}\n")
