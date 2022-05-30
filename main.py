# importar a biblioteca
from tkinter import *



# back-end
def imprimir():
    label1['text'] = entry1.get()



#front-end
#criar a janela
janela = Tk()
janela.geometry('400x400+100+500')
janela.minsize(width=400, height=200)
janela.maxsize(width=800, height=400)
janela.config(bg='yellow')


# criar os widgets
label1 = Label(janela, text= 'Olá mundo!', font= 'Arial 36')
entry1 = Entry(janela, font= 'Arial 36')
btn1 = Button(janela, text= 'Sair', font='Arial 36', command=quit)
btn2 = Button(janela, text= 'Imprimir', font='Arial 36', command=imprimir)

# organizar os widgets
label1.pack()
entry1.pack()
btn1.pack()
btn2.pack()

#executar a janela
janela.mainloop()