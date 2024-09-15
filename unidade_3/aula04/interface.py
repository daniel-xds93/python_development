from tkinter import *

import pandas as pd

class Aplicacao:
    def __init__(self):

        self.layout = Tk()

        self.layout.title("Gerador de Relatorios")

        self.layout.geometry("350x80")

        self.tela = Frame(self.layout)

        self.descricao = Label(self.tela, text="Exportar arquivo .csv:")
        self.exportar = Button(self.tela, text="Gerar arquivo", command=self.exportar_arquivo)

        self.tela.pack()
        self.descricao.pack()
        self.exportar.pack()

        mainloop()

    def exportar_arquivo(self):

        # criação de um dataframe 
        dados = pd.DataFrame(
            {   'Nome': ['Daniel', 'Vilma', 'Isabella', 'Osvaldo'],
                'Idade': [31, 36, 2, 38],
                'Sexo': ['M', 'F', 'F', 'M'] 
            }
        )

        # a linha abaixo exporta as informações
        dados.to_csv('arquivo_exportado_sem_indice.csv', index=False)

tl = Aplicacao()
