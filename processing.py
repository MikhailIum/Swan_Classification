import os
import neuro
from tkinter import ttk
from tkinter import filedialog
import shutil


def open_file(filename):
    result = neuro.start(filename)
    return result



def work_with_directory(dirname):
    dirforres = filedialog.askdirectory(title='Куда сохраним результаты?')
    ship = 0
    kric = 0
    mini = 0
    f = open('result.txt', 'w')
    for filename in os.listdir(path=dirname):
        if (filename.endswith('.png') or (filename.endswith('.jpg'))):
            result = neuro.start(dirname + '/' + filename)
            if result == "     Лебедь-\n      шипун":
                ship+=1
            elif result == "     Малый\n      лебедь":
                mini+=1
            elif result == "     Лебедь-\n      кликун":
                kric+=1
            f.write('На фото ' + filename + ' - ' + result + '\n')


    f.write("ship "+ str(ship)+" "+ "  mini: " + str(mini) + "  klick: "+str(kric))
    f.close()
    shutil.copy2('result.txt', dirforres)