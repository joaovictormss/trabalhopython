import tkinter
import PyPDF2
def LerPDF():
    print("")
def Exemplo():
    root = tkinter.Tk()
    root.title("Titulo da janela")
    root.resizable(True, True)
    
    test = tkinter.Button(root, text="Ler PDF")
    test['command'] = LerPDF
    test.pack()
    
    root.mainloop()
Exemplo()

