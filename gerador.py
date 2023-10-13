import random
import pyperclip
import customtkinter as ctk

class Senhas:
    def __init__(self):
        self.CARACTERS = 'abcdefghijklmnopqrstxyzABCDEFGHIJKLMNOPQRSTXYZ#@!'

    def gerar_senha(self):

        if self.campo_resultado:
            self.campo_resultado.pack_forget()

        self.tamanho_senha = self.campo_tamanho.get()
        self.senha = ''.join(random.choice(self.CARACTERS) for _ in range(int(self.tamanho_senha)))
        pyperclip.copy(self.senha)
        self.campo_resultado = ctk.CTkLabel(self, text=self.senha)
        self.campo_resultado.pack()

class App(ctk.CTk, Senhas):
    def __init__(self):
        ctk.CTk.__init__(self)
        Senhas.__init__(self)
        self.configuracoes_tela_inicial()
        self.conteudo_tela()
        self.campo_resultado = None

    def configuracoes_tela_inicial(self):
        self.title('Gerador de Senhas')
        self.geometry('200x200')

    def conteudo_tela(self):
        self.campo_titulo = ctk.CTkLabel(self, text='Gerador de Senhas')
        self.campo_titulo.pack(pady=10)

        self.campo_tamanho = ctk.CTkEntry(self, placeholder_text='Tamanho da Senha')
        self.campo_tamanho.pack(pady=10)

        self.botao_gerar_senha = ctk.CTkButton(self, text='Gerar Senha', command=self.gerar_senha)
        self.botao_gerar_senha.pack(pady=10)


if __name__=='__main__':
    app = App()
    app.mainloop()
