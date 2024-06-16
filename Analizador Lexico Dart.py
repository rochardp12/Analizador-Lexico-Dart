#Nombre: Roberto Encalada
#Matricula: 202101507
from datetime import datetime
import os
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
    'COMMA',
    'EQUALS',
    'NEQ',
    'DOT',
    'TWODOTS',
    'DOTCOMMA',
    'APHOSTROPHE',
    'DOUBLEAPHOSTROPHE',
    'CHAINCHARACTER',
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
t_DOT = r'\.'
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
    r'\d+\.\d+'
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

#Generate logs
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

usuarioGit = "rocaenca"
current_time = datetime.now().strftime("%d%m%Y-%Hh%M")
log_filename = f"lexico-{usuarioGit}-{current_time}.txt"
log_filepath = os.path.join(log_dir, log_filename)


AlgoritmoRoberto = """
/* Block comment example
This is a test for the block comment token.
*/

// Line comment example
public class TestClass {
    private int number = 42;
    public double decimalNumber = 3.14;
    protected boolean isValid = true;
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
        boolean flag = false;
        String greeting = "Hello, World!";
        char initial = 'A';
        
        if (localVar > 5 && flag == false) {
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

lexer.input(AlgoritmoRoberto)

# Tokenize
with open(log_filepath, 'w') as log_file:
  while True:
      tok = lexer.token()
      if not tok: 
          break      # No more input
      print(tok)
      log_file.write(f"{tok}\n")