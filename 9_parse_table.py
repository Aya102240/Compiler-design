import pandas as pd

# Define the grammar rules
grammar = {
    'Program': ['Stmts'],
    'Stmts': ['Stmt', 'Stmts', 'EOF'],
    'Stmt': ['Type IDENT = ([0-9]+) ;', 'IfStatement', 'PrintStatement', 'Stmts'],
    'IfStatement': ['if ( IDENT > ([0-9]+) ) { Stmts }'],
    'PrintStatement': ['print ( IDENT ) ;'],
    'Type': ['int'],
    'IDENT': ['~[a-z]']
}

# Create the table headers
terminals = sorted(set([symbol for rules in grammar.values() for rule in rules for symbol in rule if symbol.islower() or symbol.startswith('[')]))
nonterminals = list(grammar.keys())
headers = [''] + terminals + ['$']

# Create the table data
data = []
for nt in nonterminals:
    row = [nt] + ['' for _ in range(len(terminals)+1)]
    for rule in grammar[nt]:
        if rule[0].islower() or rule[0].startswith('['):
            col = terminals.index(rule[0]) + 1
            row[col] = rule
        else:
            for t in terminals:
                if t in rule:
                    col = terminals.index(t) + 1
                    row[col] = rule
    if 'EOF' in grammar[nt]:
        col = headers.index('$')
        row[col] = 'epsilon'
    data.append(row)
# Create the table
df = pd.DataFrame(data, columns=headers)
df = df.fillna('')
df.to_csv('parse_table.csv', index=False)
# Print the table
print(df)