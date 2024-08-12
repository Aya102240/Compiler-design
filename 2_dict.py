import split_lexems
import re

tokens = {
    '\~[0-9]+': 'IDENT',
    'int': 'Type',
    'print': 'PrintStatement',
    '(': 'LParen',
    ')' : 'RParen',
    '{': 'LBrace',
    '}': 'RBrace',
    ';': 'Semicolon',
    '[0-9]+': 'Num',
    '>': 'Greater',
    'if': 'IfStatement',
    '': 'epsilon'
}

def tokenization(list_lexems):
    tokens = []
    for i in range(0, len(list_lexems)):
        if list_lexems[i] == 'int':
            tokens.append(('TYPE', list_lexems[i]))
        elif list_lexems[i] == 'if':
            tokens.append(('IF', list_lexems[i]))
        elif list_lexems[i] == 'print':
            tokens.append(('PRINT', list_lexems[i]))
        elif list_lexems[i] == '(':
            tokens.append(('LPAREN', list_lexems[i]))
        elif list_lexems[i] == ')':
            tokens.append(('RPAREN', list_lexems[i]))
        elif list_lexems[i] == '{':
            tokens.append(('LBRACE', list_lexems[i]))
        elif list_lexems[i] == '}':
            tokens.append(('RBRACE', list_lexems[i]))
        elif list_lexems[i] == ';':
            tokens.append(('SEMICOLON', list_lexems[i]))
        elif list_lexems[i] == '=':
            tokens.append(('EQUALS', list_lexems[i]))
        elif list_lexems[i] == '>':
            tokens.append(('GREATER', list_lexems[i]))
        elif list_lexems[i] == '+':
            tokens.append(('PLUS', list_lexems[i]))
        elif list_lexems[i] == '-':
            tokens.append(('MINUS', list_lexems[i]))
        elif re.match(r'\~[a-z]', list_lexems[i]):
            tokens.append(('IDENT', list_lexems[i]))
        elif re.match(r'[0-9]+', list_lexems[i]):
            tokens.append(('NUM', list_lexems[i]))
    tokens.append(('', 'epsilon'))
    return tokens

source = 'source_code.txt'
lexems = split_lexems.lexical_analyzer(input_source_path=source)
tokenss = tokenization(lexems)
print(tokenss)