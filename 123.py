import tkinter
import PyPDF2
import requests
import re

def Leitor(in_PdfFile):  
    reader = PyPDF2.PdfReader(in_PdfFile) 
    print(reader.pages[0].extract_text())


    url = "https://date.nager.at/api/v3/PublicHolidays/2025/BR"

    payload = {}
    headers = {
  'accept': 'application/json',
  'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
  }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    feriado= reader.pages[0].extract_text().split("\n")
    for data in feriado:
        if data.strip() in response.text:
            print (data)


def LerPDF():
    Leitor(r"C:\Users\Aluno.ESTACIOACAD\Downloads\Trabalho\Trabalho\Lista de datas.pdf")


def Exemplo():
    root = tkinter.Tk()
    root.title("Título da Janela")
    root.resizable(True, True)

    
    entrada = tkinter.Entry(root, width=40)
    entrada.pack(pady=10)

    
    test = tkinter.Button(root, text="Ler PDF", command=LerPDF)
    test.pack(pady=10)

    root.mainloop()

Exemplo()


