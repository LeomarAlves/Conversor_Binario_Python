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

def decimal_para_hexadecimal(decimal):
    if decimal == 0:
        return "0"

    pilha_hex = []
    mapa_hex = {10: "A", 11: "B", 12:"C", 13:"D", 14:"E", 15:"F"}

    while decimal > 0:
        resto = decimal % 16

        if resto >=10:
            caractere = mapa_hex[resto]
        else:
            caractere = str(resto)

        pilha_hex.append(caractere)
        decimal = decimal // 16

    resultado = ""
    while len(pilha_hex) > 0:
        resultado = resultado + pilha_hex.pop()

    return resultado

def hexadecimal_para_decimal(hexadecimal):
    decimal = 0
    texto_invertido = hexadecimal[::-1]
    mapa_dec = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    for posicao in range(len(texto_invertido)):
        caractere = texto_invertido[posicao].upper()

        if caractere in mapa_dec:
            valor_digito = mapa_dec[caractere]
        else:
            valor_digito = int(caractere)

        valor_posicao =  valor_digito * (16 ** posicao)
        decimal += valor_posicao

    return str(decimal)






