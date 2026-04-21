import tkinter as tk
from logging import config
from tkinter import Entry
from main import decimal_para_binario, binario_para_decimal


def acao_converter(event=None):
    escolha = selecao.get()
    entrada = entrada_numero.get()

    try:
        if escolha == 1:
            numero = int(entrada)
            resultado = decimal_para_binario(numero)
            label_resultado.config(text="Binário: " + resultado)
        elif escolha == 2:
            resultado = binario_para_decimal(entrada)
            label_resultado.config(text="Decimal: " + resultado)
    except ValueError:
          label_resultado.config(text="Entrada inválida!")

janela = tk.Tk()
janela.title("Conversor Binário/Decimal")
janela.geometry("600x400")

label_instrucao = tk.Label(janela, text="Digite o número: ")
label_instrucao.pack()

selecao = tk.IntVar()
selecao.set(1)
botao_selecao_bin = tk.Radiobutton(janela, text="Decimal para Binário", variable=selecao, value=1)
botao_selecao_bin.pack()
botao_selecao_dec = tk.Radiobutton(janela, text="Binário para Decimal", variable=selecao, value=2)
botao_selecao_dec.pack()




entrada_numero = tk.Entry(janela)
entrada_numero.pack()
entrada_numero.bind("<Return>", acao_converter)

botao_converter = tk.Button(janela, text="Converter", command=acao_converter)
botao_converter.pack()

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

janela.mainloop()