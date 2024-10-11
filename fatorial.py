def fatorial(n, soma = 1):
    if n == 0:
        return soma
    soma *= n
    return fatorial(n - 1, soma)