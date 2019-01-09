import Tkinter as tk
class make_image:
    def __init__(self,size,root,size_pixel):
        self.size_pixel=size_pixel
        self.size=size
        self.board=tk.Canvas(root,width=(size[0]*size_pixel),height=(size[1]*size_pixel))
        
        self.mouse_button=False

        self.board.bind("<Button 1>",lambda e:self.status_mouse("press"))
        self.board.bind("<ButtonRelease 1>",lambda e:self.status_mouse("release"))
        self.board.bind('<Motion>', self.update)
        self.clean=tk.Button(root,text="clean",command=self.clean_all)
        self.clean.grid(row=0,column=1)
        self.make()
        
    def make(self):
        self.pixels={}
        for y in range(self.size[1]):
            for x in range(self.size[1]):
                self.pixels[(x,y)]=self.board.create_rectangle(0,0,self.size_pixel,self.size_pixel,fill="white")
                self.board.move(self.pixels[(x,y)],x*self.size_pixel,y*self.size_pixel)
        self.board.grid(row=0,column=0)
        
    def status_mouse(self,command):
           if command=="press":
              self.mouse_button=True
           elif command=="release":
              self.mouse_button=False
        

    def update(self,event):
        if self.mouse_button==True:
            x=int(event.x/self.size_pixel)
            y=int(event.y/self.size_pixel)

            if x>=0.0 and x<self.size[0]*self.size_pixel and y>=0.0 and y<self.size[1]*self.size_pixel:
               self.board.itemconfig(self.pixels[(x,y)],fill="black")

    def clean_all(self):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
               self.board.itemconfig(self. pixels[(x,y)],fill="white")
               
    def save(self):
        image=[]
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                color=float((self.board.itemcget(self.pixels[(x,y)],"fill")=="black"))
                image.extend([color])
      
        return image
