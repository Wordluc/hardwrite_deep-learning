import Tkinter
from make_image import make_image as make
from sklearn import neural_network
from sklearn.externals import joblib


class detection:
    def __init__(self,size,rate,n_alpha,root,S,name_file):
        self.size=size
        self.learn=neural_network.MLPClassifier(hidden_layer_sizes=S,max_iter=200,activation='logistic',verbose=True,alpha=n_alpha,learning_rate_init=rate)
        self.image=make(size,root,10.0)
        self.name_file=name_file+".joblib"
        self.compute=Tkinter.Button(root,text="compute",command=self.compute)
        self.compute.grid(row=3,column=0)
        self.result=Tkinter.Label(root,text="None")
        self.result.grid(row=3,column=1)
        self.active=False
      
     
    def compute(self):
        if self.active==True:
           test_image=self.image.save()
           predict=(self.learn.predict([test_image]))
           self.result.config(text=predict)
        else:
           print("wait learn or load a model")
        
    def new(self,training_set,n_iter):
           print("learn start")
           self.learn.max_iter=int(n_iter)
           self.learn.fit(training_set["x"],training_set["y"])
           return self.learn.loss_curve_
    def load(self):
        self.active=True
        print(self.name_file)
        self.learn=joblib.load(self.name_file)
    def save(self):
        self.active=True
        joblib.dump(self.learn,self.name_file)
    def score(self,training_set):
        return self.learn.score (training_set["x"],training_set["y"])


