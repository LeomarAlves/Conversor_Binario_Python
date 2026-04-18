def decimal_para_binario(numero):
    if numero == 0:
        return 0

    pilha_bits = []

    while numero > 0:
        resto = numero % 2
        pilha_bits.append(resto)
        numero = numero // 2

    resultado = ""
    while len(pilha_bits) > 0:
        bit = pilha_bits.pop()
        resultado = resultado + str(bit)

    return resultado

