#  доп файл с созданием txt файлов для работы 

import tkinter as tk

def filesave():
    secrets2 = open('DSD.txt','w')  # открытие в режиме записи   
    secrets2.write("его нету и не будет никогда god")
    defing = tk.Tk()

    btn = tk.Button(defing, text="create file", command=filesave )
    btn.place_configure(x=23,y=23)

def textone():
    secrets3 = open('DSD2.txt','w')  # открытие в режиме записи  
    secrets3.write("слушай а ты хитрый ладно дам тебе один прикол god дамн")

def texttwo():
    secrets3 = open('Dsd3.txt','w')  # открытие в режиме записи  
    secrets3.write("bot да что-то было вроде")

def texttree():
    secrets3 = open('files2.txt','w')  # открытие в режиме записи  
    secrets3.write("знаешь что? я не убивал тех кто зашел я лишь указал правильный им путь а дальше они сами решили....")
