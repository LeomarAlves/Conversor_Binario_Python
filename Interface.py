import tkinter as tk
from tkinter import Entry
from main import decimal_para_binario

def acao_converter():
    numero = int(entrada_numero.get())

    resultado_binario = decimal_para_binario(numero)

    label_resultado.config(text="Binário: " + resultado_binario)

janela = tk.Tk()
janela.title("Conversor Decimal para Binário")
janela.geometry("600x400")

label_instrucao = tk.Label(janela, text="Digite o número decimal: ")
label_instrucao.pack()

entrada_numero = tk.Entry(janela)
entrada_numero.pack()

botao_converter = tk.Button(janela, text="Converter", command=acao_converter)
botao_converter.pack()

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

janela.mainloop()