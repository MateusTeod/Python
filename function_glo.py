x = 1 

def escopo():
    def outra_funcao():
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

escopo()