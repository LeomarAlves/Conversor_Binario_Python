from tokenize import String


def decimal_para_binario(decimal):
    if decimal == 0:
        return 0

    pilha_bits = []

    while decimal > 0:
        resto = decimal % 2
        pilha_bits.append(resto)
        decimal = decimal // 2

    resultado = ""
    while len(pilha_bits) > 0:
        bit = pilha_bits.pop()
        resultado = resultado + str(bit)

    return resultado

def binario_para_decimal(binario):
    decimal = 0
    binario_invertido = binario[::-1]

    for posicao in range(len(binario_invertido)):
        bit = int(binario_invertido[posicao])
        valor_bit = bit * (2 ** posicao)
        decimal += valor_bit

    return str(decimal)

