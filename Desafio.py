# importar a biblioteca
from tkinter import *



# back-end
def soma():
    label1['text']=int(entry1.get())+int(entry2.get())




#front-end
#criar a janela
janela = Tk()
janela.geometry('400x400+100+500')
janela.minsize(width=400, height=200)
janela.maxsize(width=800, height=400)
janela.config(bg='pink')


# criar os widgets
label1 = Label(janela, text= 'Resultado', font= 'Arial 36')
entry1 = Entry(janela, font= 'Arial 36')
entry2 = Entry(janela, font= 'Arial 36')
btn1 = Button(janela, text= 'Soma', font='Arial 36', command=soma)

# organizar os widgets
label1.pack()
entry1.pack()
entry2.pack()
btn1.pack()

#executar a janela
janela.mainloop()