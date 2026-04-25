import tkinter as tk
from logging import config
from tkinter import Entry
from main import decimal_para_binario, binario_para_decimal, decimal_para_hexadecimal, hexadecimal_para_decimal


def acao_converter(event=None):
    escolha = base_entrada.get()
    saida = base_saida.get()
    entrada = entrada_numero.get()

    try:
        if escolha == saida:
            label_resultado.config(text=entrada)
            return

        if escolha == "Decimal" and saida == "Binário":
            numero = int(entrada)
            resultado = decimal_para_binario(numero)
            label_resultado.config(text= resultado)
        elif escolha == "Binário" and saida == "Decimal":
            numero = entrada
            resultado = binario_para_decimal(numero)
            label_resultado.config(text= resultado)
        elif escolha == "Decimal" and saida == "Hexadecimal":
            numero = int(entrada)
            resultado = decimal_para_hexadecimal(numero)
            label_resultado.config(text= resultado)

        elif escolha == "Binário" and saida == "Hexadecimal":
            numero = entrada
            resultado = binario_para_decimal(numero)
            resultado = decimal_para_hexadecimal(int(resultado))
            label_resultado.config(text= resultado)

        elif escolha == "Hexadecimal" and saida == "Decimal":
            numero = entrada
            resultado = hexadecimal_para_decimal(numero)
            label_resultado.config(text= resultado)

        elif escolha == "Hexadecimal" and saida == "Binário":
            numero = entrada
            resultado = hexadecimal_para_decimal(numero)
            resultado = decimal_para_binario(int(resultado))
            label_resultado.config(text= resultado)

    except ValueError:
          label_resultado.config(text="Entrada inválida!")

janela = tk.Tk()
janela.title("Conversor Binário/Decimal")
janela.geometry("600x400")

lista_bases = ["Decimal", "Binário", "Hexadecimal"]

label_entrada = tk.Label(janela, text="Base Numérica: ")
label_entrada.pack()
base_entrada = tk.StringVar()
base_entrada.set(lista_bases[0])
menu_entrada = tk.OptionMenu(janela, base_entrada, *lista_bases)
menu_entrada.pack()

entrada_numero = tk.Entry(janela)
entrada_numero.pack()
entrada_numero.bind("<Return>", acao_converter)

label_saida = tk.Label(janela, text="Para: ")
label_saida.pack()
base_saida = tk.StringVar()
base_saida.set(lista_bases[1])
menu_saida = tk.OptionMenu(janela, base_saida, *lista_bases)
menu_saida.pack()

botao_converter = tk.Button(janela, text="Converter", command=acao_converter)
botao_converter.pack()

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

janela.mainloop()