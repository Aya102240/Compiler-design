# Lexeme: The smallest unit in the Language “programming language”.
# Token: Type of lexeme.

def lexical_analyzer(input_source_path):
    file = open(input_source_path)
    file_data = file.read()
    markers = ["=", ";", "(", "{", "}", ")", " "]
    with open(input_source_path) as f:
        with open('out.txt', 'w') as f1:
            for lexem in range(0, len(file_data)-1):
                if file_data[lexem] in markers:
                    # every space get new line
                    if file_data[lexem] == ' ':
                        f1.write('\n')
                        continue

                    if file_data[lexem] == file_data[lexem+1]:
                        f1.write(f'\n{file_data[lexem]+file_data[lexem+1]}\n')
                        continue
                    if file_data[lexem] == file_data[lexem-1]:
                        continue
                    f1.write(f'\n{file_data[lexem]}\n')
                    continue
                f1.write(file_data[lexem])
            f1.write(file_data[-1])
            

    newOne =[]
    file = open('out.txt')
    file_data = file.read()
    with open('out.txt') as fl:
        new = ''
        for i in file_data:
            if i == '\n' or i == ' ':
                newOne.append(new)
                new =''
                continue

            new = new+i
            
    # delete the additional items ''
    try_ = []
    for t in newOne:
        if t == '':
            continue
        try_.append(t)
    file = open('out.txt')
    file_data = file.read()
    try_.append(file_data[-1])
    
    return try_

lexems = lexical_analyzer(input_source_path= "source_code.txt")
# print(lexems)

def lexical_prog(the_prog):
    markers = ["=", ";", "(", "{", "}", ")", " "]
    with open('out.txt', 'w') as f1:
            for lexem in range(0, len(the_prog)-1):
                if the_prog[lexem] in markers:
                    # every space get new line
                    if the_prog[lexem] == ' ':
                        f1.write('\n')
                        continue

                    if the_prog[lexem] == the_prog[lexem+1]:
                        f1.write(f'\n{the_prog[lexem]+the_prog[lexem+1]}\n')
                        continue
                    if the_prog[lexem] == the_prog[lexem-1]:
                        continue
                    f1.write(f'\n{the_prog[lexem]}\n')
                    continue
                f1.write(the_prog[lexem])
            f1.write(the_prog[-1])
            

    newOne =[]
    file = open('out.txt')
    the_prog = file.read()
    with open('out.txt') as fl:
        new = ''
        for i in the_prog:
            if i == '\n' or i == ' ':
                newOne.append(new)
                new =''
                continue

            new = new+i
            
    # delete the additional items ''
    try_ = []
    for t in newOne:
        if t == '' or t=='\n':
            continue
        try_.append(t)
    if the_prog[-1] != '\n':
        try_.append(the_prog[-1])

    return try_