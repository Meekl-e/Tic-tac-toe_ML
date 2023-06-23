from tkinter import *


class canvas:
    def click(self, id):
        if self.btns[id].cget("text") == "":
            self.btns[id].config(text=self.type)
            self.choice = False

    def getMatrix(self):
        return [id.cget("text") for id in self.btns]

    def __init__(self,type):
        self.type = type
        self.choice = True
        self.root = Tk()
        self.btns = []

        for id in range(3):
            btns = Frame()
            for i in range(3):
                btn = Button(btns, width=8,height=5,font=("Georgia",20,"bold"), command=lambda x=len(self.btns):self.click(x))
                btn.pack(side=LEFT)
                self.btns.append(btn)
            btns.pack(fill=X)


    def update(self, btns):
        for x in range(len(btns)):
            self.btns[x].config(text=btns[x])





