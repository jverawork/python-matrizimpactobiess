input_code = ''
with open('sentenciaplsql.sql', 'r') as archivo:
        input_code = archivo.read()

import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = ['SELECT', 'FROM', 'IDENTIFIER', 'SEMICOLON']

# Expresiones regulares para tokens simples
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_SEMICOLON = r';'
t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t):
    #print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Definición de reglas
def p_plsql_block(p):
    '''plsql_block : select_statement'''
    p[0] = p[1]

def p_select_statement(p):
    '''select_statement : SELECT identifier_list FROM IDENTIFIER SEMICOLON'''
    p[0] = p[3]

def p_identifier_list(p):
    '''identifier_list : IDENTIFIER
                      | identifier_list ',' IDENTIFIER'''
    if len(p) > 2:
        p[0] = p[1] + ', ' + p[3]
    else:
        p[0] = p[1]

def p_error(p):
    print("Error de sintaxis:", p)

# Construir el analizador sintáctico
parser = yacc.yacc()

# Ejemplo de entrada PL/SQL
input_code = 'SELECT column1, column2 FROM table_name ;'

# Parsear y analizar el código PL/SQL
result = parser.parse(input_code)
if result is not None:
    print("Tablas usadas:", result)
