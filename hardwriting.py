import matplotlib.pyplot as plt
import pandas
import numpy
import Tkinter
from detection import detection


def date_set():
    date=numpy.array(pandas.read_csv("mnist_train.csv"))
    training_set={}
    training_set["x"]=numpy.zeros((len(date[:,0]),784))
    training_set["y"]=date[:,0]
    for i in range(len(date[:,1:])):
       training_set["x"][i,:]=(date[:,1:][i]/255.0)
    return training_set
def new(recognit,box_iter):
    print("wait for learn")
    n_iter=box_iter.get()
    print(n_iter)
    training_set=date_set()
    error=recognit.new(training_set,n_iter)
    plt.plot(error)
    plt.show()
    recognit.save()
    
def load(recognit):
    recognit.load()
main=Tkinter.Tk()
root=Tkinter.Toplevel(main)
recognit=detection([28,28],0.0001,0.1,root,[784,784],"model")


box_iter=Tkinter.Entry(main,width=40)
box_iter.grid(row=0,column=1)
box_iter.insert(0,"please insert the number of interactions")

botton_new=Tkinter.Button(main,command=lambda: new(recognit,box_iter),text="NEW")
botton_new.grid(row=0,column=0)

botton_load=Tkinter.Button(main,command=lambda: load(recognit),text="LOAD")
botton_load.grid(row=2,column=0)



main.mainloop()
