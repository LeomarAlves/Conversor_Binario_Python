import tkinter as tk
from logging import config
from tkinter import Entry
from main import decimal_para_binario

def acao_converter(event=None):
      try:
        numero = int(entrada_numero.get())

        resultado_binario = decimal_para_binario(numero)

        label_resultado.config(text="Binário: " + resultado_binario)
      except ValueError:
          label_resultado.config(text="Entrada inválida!")

janela = tk.Tk()
janela.title("Conversor Decimal para Binário")
janela.geometry("600x400")

label_instrucao = tk.Label(janela, text="Digite o número decimal: ")
label_instrucao.pack()

entrada_numero = tk.Entry(janela)
entrada_numero.pack()
entrada_numero.bind("<Return>", acao_converter)

botao_converter = tk.Button(janela, text="Converter", command=acao_converter)
botao_converter.pack()

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

janela.mainloop()