from anytree import Node, RenderTree
from split_lexems import lexical_analyzer
import re
source_code_path = 'source_code.txt'
lexems = lexical_analyzer(input_source_path=source_code_path)
print(lexems)

root = Node('Program')
def new(root):
    Stmt = Node('Stmt', parent=root)
    Stmts = Node('Stmts', parent=root)
    return Stmt, Stmts
Stmt, Stmts = new(root)


for to in lexems:
    if to == 'int':
        Type = Node('Type', parent=Stmt)
        var_type = Node(to, parent=Type)

        IDENT = Node('IDENT', parent=Stmt)
        iden = r"\~[a-z]"
        if re.match(iden, lexems[lexems.index(to)+1]):
            var = Node(lexems[lexems.index(to)+1], parent=IDENT)
        elif (not re.match(iden, lexems[lexems.index(to)+1])):
            RuntimeError("Invalid identifier")
            break
    if to == '=':
        Assign = Node('=', parent=Stmt)
        num = Node(lexems[lexems.index(to)+1], parent=Stmt)
        if lexems[lexems.index(to)+2] == ';':
            separate = Node(lexems[lexems.index(to)+2], parent=Stmt)
        else:
            RuntimeError("Where is the semicolon ? ';'")
            break
    
    if to == 'if':
        Stmt = Node('Stmt', parent=Stmts)
        Stmts = Node('Stmts', parent=Stmts)

        if_stmt = Node('IfStatement', parent=Stmt)
        if_ter = Node(to, parent=if_stmt)
        if lexems[lexems.index(to)+1] == '(':
            open_brack = Node(lexems[lexems.index(to)+1], parent=if_stmt)
            IDENT = Node('IDENT', parent=if_stmt)
            iden = '\~[a-z]'
            if re.match(iden, lexems[lexems.index(to)+2]):
                var = Node(lexems[lexems.index(to)+2], parent=IDENT)
            elif (not re.match(iden, lexems[lexems.index(to)+2])):
                RuntimeError("Invalid identifier")
                break
            if lexems[lexems.index(to)+3] == '>':
                logic_operator = Node('>', parent=if_stmt)
            else:
                RuntimeError("Invalid logic operator")
                break
            if re.match("([0-9]+)", lexems[lexems.index(to)+4]):
                num = Node(lexems[lexems.index(to)+4], parent=if_stmt)
            
            if lexems[lexems.index(to)+5] == ')':
                close_brack = Node(lexems[lexems.index(to)+5], parent=if_stmt)
            else:
                RuntimeError("Close if braces")
        if lexems[lexems.index(to)+6] == '{':
            curly_open = Node("{", parent=if_stmt)
        stmts = Node('Stmts', parent=if_stmt)
        stmt = Node('Stmt', parent=stmts)
        if lexems[lexems.index(to)+7] == 'print':
            print_stmt = Node("PrintStatement", parent=stmt)
            if lexems[lexems.index(to)+8] == '(':
                open_brack = Node(lexems[lexems.index(to)+8], parent=print_stmt)
            IDENT = Node('IDENT', parent= print_stmt)
            if re.match(iden, lexems[lexems.index(to)+9]):
                id = Node(lexems[lexems.index(to)+9], parent=IDENT)
            elif not re.match(iden, lexems[lexems.index(to)+9]):
                RuntimeError("Invalid identifier")
            if lexems[lexems.index(to)+10] == ')':
                close_brack = Node(lexems[lexems.index(to)+10], parent=print_stmt)
            if lexems[lexems.index(to)+11] == ';':
                separate = Node(lexems[lexems.index(to)+11], parent=print_stmt)
        if lexems[lexems.index(to)+12] =='}':
            curly_close = Node("}", parent=if_stmt)
        stmts = Node('Stmts', parent=stmts)
        end = Node("epsilon", parent=stmts)

close = Node('epsilon', parent=Stmts)       

for pre, _, node in RenderTree(root):
    print(f'{pre}{node.name}')