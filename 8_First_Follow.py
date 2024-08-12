# compute the first and follow sets:

def first_set(grammar):
    first = {}
    for non_terminal in grammar:
        first[non_terminal] = set()

    changed = True
    while changed:
        changed = False
        for non_terminal, productions in grammar.items():
            for production in productions:
                if not production:
                    first[non_terminal].add("ε")
                    changed = True
                else:
                    for symbol in production:
                        if symbol in grammar:
                            new_symbols = first[symbol] - first[non_terminal]
                            if new_symbols:
                                first[non_terminal].update(new_symbols)
                                changed = True
                            if "ε" not in first[symbol]:
                                break
                        else:
                            first[non_terminal].add(symbol)
                            break

    return first

def follow_set(grammar, first):
    follow = {}
    for non_terminal in grammar:
        follow[non_terminal] = set()

    follow["Program"].add("$")

    changed = True
    while changed:
        changed = False
        for non_terminal, productions in grammar.items():
            for production in productions:
                for i, symbol in enumerate(production):
                    if symbol in grammar:
                        next_symbols = production[i + 1 :]
                        if next_symbols:
                            new_symbols = first_set_of_string(next_symbols, first) - follow[symbol]
                            if new_symbols:
                                follow[symbol].update(new_symbols)
                                changed = True
                        else:
                            new_symbols = follow[non_terminal] - follow[symbol]
                            if new_symbols:
                                follow[symbol].update(new_symbols)
                                changed = True

    return follow

def first_set_of_string(string, first):
    result = set()
    for symbol in string:
        if symbol in first:
            result.update(first[symbol])
            if "ε" not in first[symbol]:
                break
        else:
            result.add(symbol)
            break

    return result

grammar = {
    'Program': ['Stmts'],
    'Stmts': ['Stmt', 'Stmts', 'EOF'],
    'Stmt': ['Type IDENT = ([0-9]+) ;', 'IfStatement', 'PrintStatement', 'Stmts'],
    'IfStatement': ['if ( IDENT > ([0-9]+) ) { Stmts }'],
    'PrintStatement': ['print ( IDENT ) ;'],
    'Type': ['int'],
    'IDENT': ['~[a-z]']
}



#  we can now compute the first and follow sets for our grammar:
first_sets = first_set(grammar)
follow_sets = follow_set(grammar, first_sets)

print("First sets:", first_sets)
print("Follow sets:", follow_sets)