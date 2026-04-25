import customtkinter as ctk
from main import decimal_para_binario, binario_para_decimal, decimal_para_hexadecimal, hexadecimal_para_decimal

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Conversor de Bases Numéricas")
        self.geometry("450x550")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.lista_bases = ["Decimal", "Binário", "Hexadecimal"]

        self.label_titulo = ctk.CTkLabel(self, text="Conversor de Bases", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_titulo.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.label_instrucao = ctk.CTkLabel(self, text="Selecione a base de entrada:")
        self.label_instrucao.grid(row=1, column=0, padx=20, pady=5)

        self.base_entrada = ctk.StringVar(value=self.lista_bases[0])
        self.menu_entrada = ctk.CTkOptionMenu(self, values=self.lista_bases, variable=self.base_entrada)
        self.menu_entrada.grid(row=2, column=0, padx=20, pady=10)

        self.entrada_numero = ctk.CTkEntry(self, placeholder_text="Digite o número...")
        self.entrada_numero.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.entrada_numero.bind("<Return>", self.acao_converter)

        self.label_para = ctk.CTkLabel(self, text="Para a base:")
        self.label_para.grid(row=4, column=0, padx=20, pady=5)

        self.base_saida = ctk.StringVar(value=self.lista_bases[1])
        self.menu_saida = ctk.CTkOptionMenu(self, values=self.lista_bases, variable=self.base_saida)
        self.menu_saida.grid(row=5, column=0, padx=20, pady=10)

        self.botao_converter = ctk.CTkButton(self, text="Converter", command=self.acao_converter)
        self.botao_converter.grid(row=6, column=0, padx=20, pady=20)

        self.label_resultado = ctk.CTkLabel(self, text="Resultado: ", font=ctk.CTkFont(size=16))
        self.label_resultado.grid(row=7, column=0, padx=20, pady=(10, 20))

    def acao_converter(self, event=None):
        escolha = self.base_entrada.get()
        saida = self.base_saida.get()
        entrada = self.entrada_numero.get().strip()

        if not entrada:
            self.label_resultado.configure(text="Resultado: (vazio)", text_color="orange")
            return

        try:
            resultado = ""
            if escolha == saida:
                resultado = entrada
            
            elif escolha == "Decimal":
                numero = int(entrada)
                if saida == "Binário":
                    resultado = decimal_para_binario(numero)
                elif saida == "Hexadecimal":
                    resultado = decimal_para_hexadecimal(numero)
            
            elif escolha == "Binário":
                if saida == "Decimal":
                    resultado = binario_para_decimal(entrada)
                elif saida == "Hexadecimal":
                    dec = binario_para_decimal(entrada)
                    resultado = decimal_para_hexadecimal(int(dec))
            
            elif escolha == "Hexadecimal":
                if saida == "Decimal":
                    resultado = hexadecimal_para_decimal(entrada)
                elif saida == "Binário":
                    dec = hexadecimal_para_decimal(entrada)
                    resultado = decimal_para_binario(int(dec))

            self.label_resultado.configure(text=f"Resultado: {resultado}", text_color=("black", "white"))

        except ValueError:
            self.label_resultado.configure(text="Entrada inválida!", text_color="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()
