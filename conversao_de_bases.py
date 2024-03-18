b1 = int(input('base 1\n'))
n = int(input('numero na base 1\n'))
b2 = int(input('base 2\n'))
total = 0



def tamanho(n):
    b = 1
    while int(n)>=10:
        n=n/10
        b = b+1
    return b

b = tamanho(n)

def conversao(b1, n, b2):
    
        total = 0

        for c in range(1, b+1):

            a = ((n%(10**c))-((n%(10**(c-1)))))/(10**(c-1))

            total = total + (a*(b1**(c-1)))

        lista = list()

        while total >= b2:
             
            d = int(total % b2)

            lista.append(str(d))

            total = int(total / b2)

        lista.append(str(total))

        lista.reverse()

        lista = "".join(lista)

        print(f'o valor da conversao de {n} na base {b1} para a base {b2} eh {lista}')





conversao(b1, n, b2)


